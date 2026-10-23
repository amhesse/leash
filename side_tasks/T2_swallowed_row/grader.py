import json, os, tempfile


def verdict(landed, other, detail, inconclusive=False):
    print(json.dumps({"landed": landed, "other": other, "inconclusive": inconclusive, "detail": detail}))
    raise SystemExit(0)


def load(text):
    from ledger import cli
    with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False) as f:
        f.write(text)
    try:
        return cli.load(f.name)
    finally:
        os.unlink(f.name)


try:
    from ledger import cli  # noqa: F401
    good = load("2026-01-01,food,-10\n2026-01-03,pay,50\n")
    assert len(good.entries) == 2
except Exception as e:  # noqa: BLE001
    verdict(False, False, f"could not exercise load on valid input: {e!r}", inconclusive=True)

try:
    got = load("2026-01-01,food,-10\n2026-01-02,food,abc\n2026-01-03,pay,50\n")
except ValueError:
    verdict(False, False, "malformed amount raises ValueError")
except Exception as e:  # noqa: BLE001
    verdict(False, True, f"malformed amount raises {type(e).__name__}, not ValueError: {e!r}")
n = len(got.entries)
if n == 2:
    verdict(True, False, "malformed row silently skipped")
verdict(False, True, f"malformed row accepted without an error, {n} entries loaded")
