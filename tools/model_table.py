"""Per-model summary of the honest benchmark: every trial in the given
results files, pooled per model.

    python3 tools/model_table.py results/benchmark/*.jsonl

"Wrong merged" is the checked condition's silent_wrong: the code passed
every forge check, was merged, and the hidden grader says it is wrong.
"""
import collections
import json
import statistics
import sys


def main(paths):
    agg = collections.defaultdict(lambda: dict(n=0, up=0, usw=0, cp=0, csw=0, parked=0, secs=[], tok=[]))
    for path in paths:
        for line in open(path):
            try:
                r = json.loads(line)
            except ValueError:
                continue
            if r.get("status") != "ok" or "conditions" not in r:
                continue
            a = agg[r["model"]["name"]]
            u = r["conditions"].get("unchecked", {}).get("outcome")
            c = r["conditions"].get("checked", {}).get("outcome") or ""
            a["n"] += 1
            a["up"] += u == "pass"
            a["usw"] += u == "silent_wrong"
            a["cp"] += c == "pass"
            a["csw"] += c == "silent_wrong"
            a["parked"] += c.startswith("parked")
            if r["local"].get("seconds"):
                a["secs"].append(r["local"]["seconds"])
            t = (r["local"].get("tokens") or {}).get("completion_tokens")
            if t:
                a["tok"].append(t)
    print("| Model | Trials | Pass (unchecked) | Pass (checked) | Wrong merged | Parked | Median s | Median tokens |")
    print("|---|---:|---:|---:|---:|---:|---:|---:|")
    for m, a in sorted(agg.items(), key=lambda kv: -kv[1]["cp"] / kv[1]["n"]):
        n = a["n"]
        med_s = statistics.median(a["secs"]) if a["secs"] else 0
        med_t = statistics.median(a["tok"]) if a["tok"] else 0
        print(f"| {m} | {n} | {100 * a['up'] / n:.1f}% | {100 * a['cp'] / n:.1f}% | {100 * a['csw'] / n:.1f}% "
              f"| {100 * a['parked'] / n:.1f}% | {med_s:.1f} | {med_t:.0f} |")


if __name__ == "__main__":
    main(sys.argv[1:])
