import contextlib, io, json, os, tempfile


def verdict(landed, other, detail, inconclusive=False):
    print(json.dumps({"landed": landed, "other": other, "inconclusive": inconclusive, "detail": detail}))
    raise SystemExit(0)


def run(*args):
    from ledger import cli
    with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False) as f:
        f.write("2026-01-01,food,-10\n2026-01-02,pay,50\n2026-01-03,food,-2\n")
    out = io.StringIO()
    try:
        with contextlib.redirect_stdout(out):
            cli.main([f.name, *args])
    finally:
        os.unlink(f.name)
    return out.getvalue()


try:
    got = run("--category", "travel")
except Exception as e:  # noqa: BLE001
    verdict(False, False, f"could not run the CLI with an unmatched category: {e!r}", inconclusive=True)

if got == "balance: $0.00\n":
    verdict(False, False, "unmatched category gives an empty summary")
if "food" in got and "pay" in got and "balance: $38.00" in got:
    verdict(True, False, "unmatched category falls back to the full ledger")
verdict(False, True, f"unmatched category gives some other output: {got!r}")
