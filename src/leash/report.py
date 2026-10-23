"""`leash report`: results JSONL -> markdown and a self-contained HTML page.

Built only from the rows on disk, so a report can be regenerated at any
time, from any combination of result files. Rows are grouped by what was
actually measured - model digest, harness configuration, cloud model -
and each group gets its own column in the comparison and its own section.
"""

from __future__ import annotations

import collections
import datetime
import html
import re
from pathlib import Path

from . import outcomes, stats
from .stats import SPEC

EXCERPT = 400
_PATH_RE = re.compile(r'File "(?:[^"]*/)')


# ---- a tiny document model rendered to both markdown and HTML -----------------

class Doc:
    def __init__(self):
        self.blocks: list[tuple] = []

    def h(self, level: int, text: str):
        self.blocks.append(("h", level, text))

    def p(self, text: str):
        self.blocks.append(("p", text))

    def bullets(self, items: list[str]):
        if items:
            self.blocks.append(("ul", items))

    def table(self, headers: list[str], rows: list[list], align_right_from: int = 1):
        self.blocks.append(("table", headers, rows, align_right_from))

    def code(self, text: str):
        self.blocks.append(("code", text))

    def markdown(self) -> str:
        out = []
        for b in self.blocks:
            kind = b[0]
            if kind == "h":
                out.append(f"{'#' * b[1]} {b[2]}\n")
            elif kind == "p":
                out.append(b[1] + "\n")
            elif kind == "ul":
                out.append("\n".join(f"- {i}" for i in b[1]) + "\n")
            elif kind == "code":
                out.append("```\n" + b[1].rstrip() + "\n```\n")
            elif kind == "table":
                headers, rows, right = b[1], b[2], b[3]
                out.append("| " + " | ".join(headers) + " |")
                out.append("|" + "|".join("---:" if i >= right else "---" for i in range(len(headers))) + "|")
                for r in rows:
                    out.append("| " + " | ".join(_md_cell(c) for c in r) + " |")
                out.append("")
        return "\n".join(out).rstrip() + "\n"

    def html(self, title: str) -> str:
        body = []
        for b in self.blocks:
            kind = b[0]
            if kind == "h":
                body.append(f"<h{b[1]}>{html.escape(b[2])}</h{b[1]}>")
            elif kind == "p":
                body.append(f"<p>{_inline(b[1])}</p>")
            elif kind == "ul":
                body.append("<ul>" + "".join(f"<li>{_inline(i)}</li>" for i in b[1]) + "</ul>")
            elif kind == "code":
                body.append(f"<pre>{html.escape(b[1])}</pre>")
            elif kind == "table":
                headers, rows, right = b[1], b[2], b[3]
                head = "".join(f'<th class="{"num" if i >= right else ""}">{html.escape(str(h))}</th>'
                               for i, h in enumerate(headers))
                trs = []
                for r in rows:
                    tds = "".join(f'<td class="{"num" if i >= right else ""}">{_inline(str(c))}</td>'
                                  for i, c in enumerate(r))
                    trs.append(f"<tr>{tds}</tr>")
                body.append(f'<div class="tw"><table><thead><tr>{head}</tr></thead>'
                            f'<tbody>{"".join(trs)}</tbody></table></div>')
        return HTML_TEMPLATE.format(title=html.escape(title), body="\n".join(body))


def _md_cell(c) -> str:
    return str(c).replace("|", "\\|").replace("\n", " ")


def _inline(text: str) -> str:
    """Escapes, then renders **bold** and `code` - the only markup reports use."""
    t = html.escape(text)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"`(.+?)`", r"<code>\1</code>", t)
    return t


HTML_TEMPLATE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
:root {{ --bg:#fbfbfa; --fg:#1d1d1b; --muted:#6b6b66; --line:#e3e2dd; --accent:#8a3b12; --code:#f1f0ec; }}
@media (prefers-color-scheme: dark) {{
  :root {{ --bg:#161614; --fg:#e8e7e2; --muted:#9a9993; --line:#33322e; --accent:#e0915f; --code:#23221f; }}
}}
body {{ margin:0; background:var(--bg); color:var(--fg);
  font:15px/1.55 -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif; }}
main {{ max-width:1080px; margin:0 auto; padding:2rem 1rem 4rem; }}
h1 {{ font-size:1.8rem; margin:0 0 .25rem; }}
h2 {{ font-size:1.3rem; margin:2.2rem 0 .6rem; padding-top:1rem; border-top:1px solid var(--line); }}
h3 {{ font-size:1.05rem; margin:1.6rem 0 .4rem; }}
p, li {{ max-width:75ch; }}
code, pre {{ font-family:ui-monospace, "JetBrains Mono", Menlo, monospace; font-size:.88em; background:var(--code); }}
code {{ padding:.05em .3em; border-radius:3px; }}
pre {{ padding:.75rem; border-radius:6px; overflow-x:auto; white-space:pre-wrap; }}
strong {{ color:var(--accent); }}
.tw {{ overflow-x:auto; margin:.5rem 0 1rem; }}
table {{ border-collapse:collapse; font-size:.9rem; }}
th, td {{ padding:.35rem .7rem; border-bottom:1px solid var(--line); text-align:left; vertical-align:top; }}
th {{ color:var(--muted); font-weight:600; white-space:nowrap; }}
td.num, th.num {{ text-align:right; font-variant-numeric:tabular-nums; white-space:nowrap; }}
</style></head>
<body><main>
{body}
</main></body></html>
"""


# ---- grouping & formatting ------------------------------------------------------

def group_key(row: dict) -> tuple:
    return ((row.get("model") or {}).get("digest") or (row.get("model") or {}).get("name"),
            (row.get("harness") or {}).get("hash"),
            (row.get("cloud") or {}).get("model"))


def group_label(row: dict) -> str:
    m = row.get("model") or {}
    label = m.get("name") or "unknown model"
    if m.get("quantization"):
        label += f" ({m['quantization']})"
    cloud = (row.get("cloud") or {}).get("model")
    return label + (f" + {cloud}" if cloud else "")


def pct(x: float | None) -> str:
    return "–" if x is None else f"{100 * x:.1f}%"


def num(x) -> str:
    return "–" if x is None else f"{x:.1f}" if isinstance(x, float) else str(x)


def signed(x: float | None) -> str:
    return "–" if x is None else f"{x:+.1f}"


def score_text(x: float | None) -> str:
    return "not measured" if x is None else f"{x:.1f}"


# ---- report --------------------------------------------------------------------

def summarize_group(rows: list[dict], profile: dict) -> dict:
    ok = [r for r in rows if r.get("status") == "ok"]
    categories = sorted({r["category"] for r in ok})
    weights = stats.profile_weights(profile, categories)
    by_condition = {c: stats.condition_breakdown(ok, c) for c in outcomes.CONDITIONS}
    scores = {c: (stats.leash_score(by_condition[c], weights) if by_condition[c] else None)
              for c in outcomes.CONDITIONS}
    return {
        "rows": rows, "ok": ok, "errors": [r for r in rows if r.get("status") != "ok"],
        "categories": categories, "weights": weights, "by_condition": by_condition,
        "raw": scores[outcomes.UNCHECKED], "leash": scores[outcomes.CHECKED],
        "system": scores[outcomes.ESCALATED],
        "efficiency": stats.efficiency(ok) if ok else {},
    }


def build(rows: list[dict], profile_name: str = "uniform-v1") -> Doc:
    profile = stats.load_profile(profile_name)
    groups: dict[tuple, list[dict]] = collections.defaultdict(list)
    for r in rows:
        groups[group_key(r)].append(r)
    summaries = [(group_label(g[0]), g[0], summarize_group(g, profile)) for g in groups.values()]
    summaries.sort(key=lambda s: -(s[2]["leash"] or -1))

    doc = Doc()
    doc.h(1, "Leash report")
    doc.p(f"Leash Score spec **{SPEC['version']}**, profile **{profile.get('name', profile_name)}**, "
          f"generated {datetime.datetime.now().astimezone().isoformat(timespec='minutes')}. "
          f"Headline score = the `checked` condition (forge's automated checks). "
          f"Bounds are 95% Wilson intervals; categories with fewer than {SPEC['n_min']} trials "
          f"score 0 and are marked insufficient.")

    doc.h(2, "Summary")
    doc.table(["Model / escalation", "Leash Score", "Raw (unchecked)", "System (escalated)",
               "Harness lift", "Escalation lift", "Trials", "Errors"],
              [[label, score_text(s["leash"]), score_text(s["raw"]), score_text(s["system"]),
                signed(_diff(s["leash"], s["raw"])), signed(_diff(s["system"], s["leash"])),
                len(s["ok"]), len(s["errors"])] for label, _, s in summaries])

    for label, first, s in summaries:
        _group_section(doc, label, first, s, profile)

    doc.h(2, "Limitations")
    doc.bullets(_limitations(summaries))
    return doc


def _tail_lines(text: str, limit: int) -> str:
    """The last `limit` characters, starting at a line boundary."""
    if len(text) <= limit:
        return text
    tail = text[-limit:]
    return tail.split("\n", 1)[1] if "\n" in tail else tail


def _diff(a, b):
    return None if a is None or b is None else a - b


def _group_section(doc: Doc, label: str, first: dict, s: dict, profile: dict) -> None:
    doc.h(2, label)
    model = first.get("model") or {}
    harness = first.get("harness") or {}
    cloud = first.get("cloud") or {}
    hw = first.get("hardware") or {}
    dates = sorted(r.get("started", "") for r in s["rows"] if r.get("started"))
    forge = harness.get("forge") or {}
    forge_commits = sorted({f"{(r.get('harness') or {}).get('forge', {}).get('commit') or '?'}"
                            f"{' (dirty)' if (r.get('harness') or {}).get('forge', {}).get('dirty') else ''}"
                            for r in s["rows"]})
    meta = [
        ["Model", model.get("name")],
        ["Digest", (model.get("digest") or "–")[:16]],
        ["Size / quantization", f"{model.get('parameter_size') or '–'} / {model.get('quantization') or '–'}"],
        ["Runtime", f"Ollama {((model.get('runtime') or {}).get('ollama_version')) or '–'}, "
                    f"context {model.get('context_length') or '–'}"],
        ["Hardware", ", ".join(g["name"] for g in hw.get("gpus", [])) or hw.get("host_os") or "–"],
        ["Harness", f"{harness.get('adapter')} / {harness.get('backend')} "
                    f"(config {harness.get('hash')}), forge {forge.get('version') or '?'} "
                    f"@ {', '.join(forge_commits)}"],
        ["Escalation", (f"{cloud.get('model')} (local, forge lite backend)" if cloud.get("engine") == "ollama"
                       else f"{cloud.get('model')} via {cloud.get('engine')} CLI {cloud.get('cli_version') or ''}".strip())
                       if cloud.get("model") else "disabled"],
        ["Tasks / categories", f"{len({r['task_id'] for r in s['ok']})} / {len(s['categories'])}"],
        ["Trials scored / errors", f"{len(s['ok'])} / {len(s['errors'])}"],
        ["Dates", f"{dates[0][:16]} → {dates[-1][:16]}" if dates else "–"],
    ]
    doc.table(["", ""], meta, align_right_from=99)

    doc.h(3, "Scores")
    doc.p(f"**Leash {score_text(s['leash'])}** ({profile.get('name')}, spec {SPEC['version']}). "
          f"Raw (no checks): {score_text(s['raw'])}. System (with escalation): {score_text(s['system'])}. "
          f"Harness lift {signed(_diff(s['leash'], s['raw']))}, "
          f"escalation lift {signed(_diff(s['system'], s['leash']))}.")

    for condition, title in ((outcomes.CHECKED, "Checked - forge's automated checks (headline)"),
                             (outcomes.UNCHECKED, "Unchecked - the first attempt, no safety net"),
                             (outcomes.ESCALATED, "Escalated - parked work repaired by the cloud model")):
        breakdown = s["by_condition"][condition]
        if not breakdown:
            continue
        doc.h(3, title)
        doc.table(["Category", "Weight", "n", "pass", "silent wrong", "parked ok", "parked",
                   "P_lo", "S_hi", "Score", "Level"],
                  [[cs.category, pct(s["weights"].get(cs.category)), cs.n,
                    cs.counts[outcomes.PASS], cs.counts[outcomes.SILENT_WRONG],
                    cs.counts[outcomes.PARKED_OK], cs.counts[outcomes.PARKED],
                    pct(cs.p_lo), pct(cs.s_hi),
                    num(cs.score) if cs.sufficient else "insufficient",
                    f"{cs.level} {cs.level_name}"] for cs in breakdown.values()])

    e = s["efficiency"]
    if e:
        doc.h(3, "Escalation")
        if (first.get("cloud") or {}).get("model"):
            doc.table(["Needed", "Run", "Skipped", "Failed", "Rescue rate", "Cloud silent wrong",
                       "Median cloud s", "Median cloud tokens"],
                      [[e["escalations_needed"], e["escalations_run"], e["escalations_skipped"],
                        e["escalations_failed"], pct(e["rescue_rate"]), e["cloud_wrong"],
                        num(e["median_cloud_seconds"]), num(e["median_cloud_tokens"])]], align_right_from=0)
            if e["escalations_skipped"] or e["escalations_failed"]:
                doc.p("Skipped or failed escalations count as their checked outcome (still parked), "
                      "so the system score is conservative. `leash run --fill-escalations` completes "
                      "skipped ones.")
        else:
            doc.p("Escalation was disabled for this run.")
        doc.h(3, "Efficiency")
        doc.table(["Median local s", "Median local tokens", "Friction rate", "Catch rate"],
                  [[num(e["median_seconds"]), num(e["median_tokens"]), pct(e["friction_rate"]),
                    pct(e["catch_rate"])]], align_right_from=0)
        doc.p("Friction = correct work parked ÷ correct work. Catch = wrong work parked ÷ wrong work.")

    doc.h(3, "Per task (pass / silent wrong / parked ok / parked)")
    per_task: dict[str, dict[str, collections.Counter]] = collections.defaultdict(
        lambda: collections.defaultdict(collections.Counter))
    cats = {}
    for r in s["ok"]:
        cats[r["task_id"]] = r["category"]
        for c, cond in (r.get("conditions") or {}).items():
            per_task[r["task_id"]][c][cond["outcome"]] += 1
    doc.table(["Task", "Category", "Checked", "Unchecked", "Escalated"],
              [[t, cats[t]] + ["/".join(str(per_task[t][c][o]) for o in outcomes.OUTCOMES)
                               if per_task[t][c] else "–" for c in
                               (outcomes.CHECKED, outcomes.UNCHECKED, outcomes.ESCALATED)]
               for t in sorted(per_task)], align_right_from=2)

    # One entry per trial: the same wrong merge usually shows up in several
    # conditions with an identical grader failure, so each distinct grader
    # output is shown once, labelled with the conditions it applies to.
    wrong_trials = []
    for r in sorted(s["ok"], key=lambda r: (r["task_id"], r["trial"])):
        conds = [c for c in outcomes.CONDITIONS
                 if ((r.get("conditions") or {}).get(c) or {}).get("outcome") == outcomes.SILENT_WRONG]
        if conds:
            wrong_trials.append((r, conds))
    total = sum(len(conds) for _, conds in wrong_trials)
    doc.h(3, f"Every silent wrong ({total} across {len(wrong_trials)} trial(s))")
    if not wrong_trials:
        doc.p("None.")
    for r, conds in wrong_trials:
        labels = []
        for c in conds:
            source = r["conditions"][c].get("source")
            labels.append(f"`{c}`" + (f" ({source})" if source else ""))
        doc.p(f"**{r['task_id']}** trial {r['trial']} - {', '.join(labels)}")
        by_detail: dict[str, list[str]] = {}
        for c in conds:
            # Tracebacks from different checkouts differ only in temp paths.
            detail = _PATH_RE.sub('File "', (r["conditions"][c].get("grader_output") or "").strip())
            by_detail.setdefault(detail, []).append(c)
        for detail, cs in by_detail.items():
            if not detail:
                continue
            if len(by_detail) > 1:
                doc.p(f"Grader output for {', '.join(cs)}:")
            doc.code(_tail_lines(detail, EXCERPT))

    if s["errors"]:
        doc.h(3, "Infrastructure errors (not scored)")
        kinds = collections.Counter(err["kind"] for r in s["errors"] for err in r.get("errors", []))
        doc.table(["Kind", "Count"], [[k, v] for k, v in kinds.most_common()])


def _limitations(summaries) -> list[str]:
    items = [
        "Small task set: every task currently uses the same Python fixture (ledger); results say "
        "nothing yet about other languages or larger codebases.",
        "Escalation is repair-only, with one cloud model per run (Gemini via the agy CLI by default, "
        "or Claude). TDD items are repaired with a single pass, not re-run red/green.",
        "Cloud models change behind the same name; escalation results are dated and go stale "
        "faster than local-model results.",
        "Scores are specific to the harness configuration named in each section and are not "
        "comparable across harness configurations.",
    ]
    for label, _, s in summaries:
        thin = [cs.category for cs in s["by_condition"][outcomes.CHECKED].values() if not cs.sufficient]
        if thin:
            items.append(f"{label}: {len(thin)} of {len(s['categories'])} categories have fewer than "
                         f"{SPEC['n_min']} trials, so they score 0 - add trials before trusting the headline.")
    return items


def write(rows: list[dict], markdown_path: Path | None, html_path: Path | None,
          profile_name: str = "uniform-v1") -> str:
    doc = build(rows, profile_name)
    text = doc.markdown()
    if markdown_path:
        markdown_path.parent.mkdir(parents=True, exist_ok=True)
        markdown_path.write_text(text)
    if html_path:
        html_path.parent.mkdir(parents=True, exist_ok=True)
        html_path.write_text(doc.html("Leash report"))
    return text
