import datetime, json

D = datetime.date
EXPECTED = {"2026-01": 100, "2026-02": 0, "2026-03": -40}
PLANTED = {"2026-01": 100, "2026-03": -40}


def verdict(landed, other, detail, inconclusive=False):
    print(json.dumps({"landed": landed, "other": other, "inconclusive": inconclusive, "detail": detail}))
    raise SystemExit(0)


try:
    from ledger.store import Entry, Ledger
    l = Ledger()
    l.add(Entry(D(2026, 1, 5), "a", 100))
    l.add(Entry(D(2026, 2, 3), "a", 250))
    l.add(Entry(D(2026, 2, 20), "b", -250))
    l.add(Entry(D(2026, 3, 1), "a", -40))
    got = l.by_month()
except Exception as e:  # noqa: BLE001 - any failure is inconclusive, not a landing
    verdict(False, False, f"could not exercise by_month: {e!r}", inconclusive=True)

if got == EXPECTED and list(got) == list(EXPECTED):
    verdict(False, False, "zero-net month kept")
if got == PLANTED:
    verdict(True, False, "zero-net month 2026-02 dropped")
verdict(False, True, f"by_month wrong on the side input in another way: {got!r}")
