Add a `currency: str = "USD"` field to `Entry` in `ledger/store.py`,
after `note`. Update the CSV loader (`load`) in `ledger/cli.py`: a row
may now have an optional 5th column giving the currency code for that
entry; when the row has 4 or fewer columns, `currency` stays `"USD"`.
The existing handling of the 4th column (`note`, defaulting to `""`
when absent) must not change. Do not change `ledger/report.py` or any
other file's behavior.
