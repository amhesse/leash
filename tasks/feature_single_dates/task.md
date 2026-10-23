In `ledger/store.py`, add a method `Ledger.by_month() -> dict[str, int]`
mapping "YYYY-MM" strings to the net cents of entries dated in that
month. Keys must be in ascending chronological order in the returned
dict. Months with no entries are omitted.
