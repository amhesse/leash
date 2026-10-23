#!/usr/bin/env python3
"""One-time port of forge's calibration bench into Leash's task format,
kept in the repo so the provenance of every task and mutant is inspectable
and re-runnable.

    python3 tools/port_forge_bench.py ~/projects/forge/bench

For each item in forge's bench/items.toml it writes tasks/<id>/ with
task.md, meta.toml, grader.py and reference/, copies the fixture to
fixtures/ledger/, and generates mutants/<name>/ overlay directories.

Mutants are plausible WRONG solutions, each derived from the reference by
an exact text substitution (asserted to apply), so a grader that can't
reject them is caught by `leash selftest`. Where forge's calibration runs
recorded a real silent_wrong answer, the mutant reproduces that failure
and is named real_*.
"""

import shutil
import sys
import tomllib
from pathlib import Path

LEASH_ROOT = Path(__file__).resolve().parents[1]

# task id -> [(mutant name, description, {file: [(old, new), ...]} | None, dropped files)]
MUTANTS = {
    "exact_new_file": [
        ("trailing_space", "Content right except a trailing space - byte-exact must reject",
         {"ledger/constants.py": [("CENTS_PER_UNIT = 100", "CENTS_PER_UNIT = 100 ")]}, []),
        ("single_quotes", "Equivalent Python, different bytes",
         {"ledger/constants.py": [('"USD"', "'USD'")]}, []),
    ],
    "exact_replace_function_file": [
        ("sign_after_dollar", 'Renders "$-1.50" instead of "-$1.50"',
         {"ledger/money.py": [('f"{sign}${cents // 100}', 'f"${sign}{cents // 100}')]}, []),
        ("no_abs", "Keeps the sign in the digits: -150 becomes \"-$-2.50\"",
         {"ledger/money.py": [("    cents = abs(cents)\n", "")]}, []),
    ],
    "small_edit_single": [
        ("no_abs", "Floor division on a negative: -150 becomes \"-$-2.50\"",
         {"ledger/money.py": [("    cents = abs(cents)\n", "")]}, []),
        ("touched_parse_amount", "Also 'fixed' parse_amount, which the task said not to change",
         {"ledger/money.py": [("return int(whole) * 100 + int(frac)",
                               'return int(whole) * 100 + int(frac.ljust(2, "0"))')]}, []),
    ],
    "add_method_single": [
        ("abs_sum", "Sums magnitudes, so spending comes out positive",
         {"ledger/store.py": [("return sum(e.cents for e in self.entries if e.category == category)",
                               "return sum(abs(e.cents) for e in self.entries if e.category == category)")]}, []),
        ("inverted_filter", "Sums every OTHER category",
         {"ledger/store.py": [("if e.category == category)", "if e.category != category)")]}, []),
    ],
    "bugfix_from_symptom": [
        ("real_padding_not_fixed", "Real calibration failure: added the ValueError but left \"12.5\" -> 1205",
         {"ledger/money.py": [('int(frac.ljust(2, "0"))', "int(frac)")]}, []),
        ("no_value_error", "Fixed the padding but never rejects a third decimal place",
         {"ledger/money.py": [("        if len(frac) > 2:\n"
                               "            raise ValueError(f\"too many decimal places: {text!r}\")\n", "")]}, []),
    ],
    "bugfix_negative_fraction": [
        ("negative_zero", "Takes the sign from int(whole), so \"-0.50\" becomes +50",
         {"ledger/money.py": [('sign = -1 if whole.startswith("-") else 1',
                               "sign = -1 if int(whole) < 0 else 1")]}, []),
        ("dropped_abs", "Applies the sign twice: \"-12.50\" becomes 1150",
         {"ledger/money.py": [("abs(int(whole)) * 100", "int(whole) * 100")]}, []),
    ],
    "algorithm_single": [
        ("smaller_first", "Right amounts, wrong order: [33, 33, 34]",
         {"ledger/money.py": [("return [base + 1] * extra + [base] * (parts - extra)",
                               "return [base] * (parts - extra) + [base + 1] * extra")]}, []),
        ("no_parts_validation", "parts=0 raises ZeroDivisionError, not ValueError",
         {"ledger/money.py": [("    if parts < 1:\n        raise ValueError(\"parts must be at least 1\")\n", "")]}, []),
    ],
    "split_evenly_signed": [
        ("real_floor_division", "Real calibration failure shape: floor divmod on a negative amount",
         {"ledger/money.py": [("    sign = -1 if cents < 0 else 1\n"
                               "    base, extra = divmod(abs(cents), parts)\n"
                               "    return [sign * (base + 1)] * extra + [sign * base] * (parts - extra)",
                               "    base, extra = divmod(cents, parts)\n"
                               "    return [base + 1] * extra + [base] * (parts - extra)")]}, []),
        ("real_sign_lost", "Real calibration failure: [33, 33, 34] for -100 - sign dropped, order reversed",
         {"ledger/money.py": [("return [sign * (base + 1)] * extra + [sign * base] * (parts - extra)",
                               "return [base] * (parts - extra) + [base + 1] * extra")]}, []),
    ],
    "feature_single_dates": [
        ("real_insertion_order", "Real calibration failure: months in insertion order, not chronological",
         {"ledger/store.py": [("for e in sorted(self.entries, key=lambda e: e.date):",
                               "for e in self.entries:")]}, []),
        ("unpadded_month", "Keys like \"2026-1\" instead of \"2026-01\"",
         {"ledger/store.py": [("{e.date.month:02d}", "{e.date.month}")]}, []),
    ],
    "multi_file_cli_flag": [
        ("real_missing_import", "Real calibration failure: cli.py lost its `summary` import",
         {"ledger/cli.py": [("from .report import summary\n", "")]}, []),
        ("mutates_original", "filtered() empties the original ledger instead of returning a copy",
         {"ledger/store.py": [("        result = Ledger()\n"
                               "        result.entries = [e for e in self.entries if e.category == category]\n"
                               "        return result",
                               "        self.entries = [e for e in self.entries if e.category == category]\n"
                               "        return self")]}, []),
    ],
    "rename_across_files": [
        ("alias_left", "Renamed, but left `add` behind as an alias",
         {"ledger/store.py": [("    def balance(self)", "    add = record\n\n    def balance(self)")]}, []),
        ("tests_not_updated", "Library renamed, tests still call .add()",
         {"tests/test_basic.py": [('ledger.record(Entry(datetime.date(2026, 1, 1), "food", 1000))',
                                   'ledger.add(Entry(datetime.date(2026, 1, 1), "food", 1000))')]}, []),
    ],
    "add_currency_field": [
        ("currency_from_note_column", "Reads currency from the 4th column",
         {"ledger/cli.py": [('currency = row[4] if len(row) > 4 else "USD"',
                            'currency = row[3] if len(row) > 3 else "USD"')]}, []),
        ("field_before_note", "Field added before `note`, so positional construction swaps them",
         {"ledger/store.py": [('    note: str = ""\n    currency: str = "USD"',
                               '    currency: str = "USD"\n    note: str = ""')]}, []),
    ],
    "tdd_budget": [
        ("real_summed_both_signs", "Real forge failure: counts income against the budget too",
         {"ledger/budget.py": [(" and e.cents < 0)", ")")]}, []),
        ("at_limit_is_over", "Spending exactly at the limit is reported as over",
         {"ledger/budget.py": [("if spent > limit:", "if spent >= limit:")]}, []),
    ],
    "tdd_average_transaction": [
        ("spending_only", "Averages spending only, the exact trap the task warns about",
         {"ledger/stats.py": [("if e.category == category]", "if e.category == category and e.cents < 0]")]}, []),
        ("no_rounding", "Returns the unrounded float",
         {"ledger/stats.py": [("return round(sum(values) / len(values), 2)",
                               "return sum(values) / len(values)")]}, []),
        ("no_test_written", "Implementation without the test the TDD task requires",
         None, ["tests/test_stats.py"]),
    ],
}


def toml_str(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def copytree_clean(src: Path, dst: Path) -> None:
    shutil.copytree(src, dst, dirs_exist_ok=True,
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        print(__doc__)
        return 2
    bench = Path(argv[0]).expanduser().resolve()
    items = tomllib.loads((bench / "items.toml").read_text())["item"]

    fixture_dst = LEASH_ROOT / "fixtures" / "ledger"
    shutil.rmtree(fixture_dst, ignore_errors=True)
    copytree_clean(bench / "fixture", fixture_dst)

    missing = sorted(set(MUTANTS) ^ {i["id"] for i in items})
    if missing:
        print(f"mutant table and items.toml disagree on: {missing}")
        return 1

    for item in items:
        tid = item["id"]
        tdir = LEASH_ROOT / "tasks" / tid
        shutil.rmtree(tdir, ignore_errors=True)
        tdir.mkdir(parents=True)
        (tdir / "task.md").write_text(item["text"].strip() + "\n")
        shutil.copy(bench / "graders" / f"{tid}.py", tdir / "grader.py")
        copytree_clean(bench / "reference" / tid, tdir / "reference")

        meta = [
            f"id = {toml_str(tid)}",
            f"category = {toml_str(item['category'])}",
            'fixture = "ledger"',
            'language = "python"',
            'visibility = "public"',
            'source = "forge/bench/items.toml"',
            "",
            "[mutants]",
        ]
        for name, desc, subs, dropped in MUTANTS[tid]:
            meta.append(f"{name} = {toml_str(desc)}")
            mdir = tdir / "mutants" / name
            copytree_clean(tdir / "reference", mdir)
            for rel in dropped:
                (mdir / rel).unlink()
            for rel, pairs in (subs or {}).items():
                path = mdir / rel
                text = path.read_text()
                for old, new in pairs:
                    if text.count(old) != 1:
                        print(f"{tid}/{name}: substitution target found {text.count(old)}x in {rel}: {old!r}")
                        return 1
                    text = text.replace(old, new)
                path.write_text(text)
        (tdir / "meta.toml").write_text("\n".join(meta) + "\n")
        print(f"ported {tid} ({len(MUTANTS[tid])} mutants)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
