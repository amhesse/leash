TDD: implement `ledger/stats.py` so `tests/test_stats.py` passes: a
function `average_transaction(ledger, category: str) -> float` takes a
`ledger.store.Ledger` and returns the average `cents` value, as a float
rounded to 2 decimal places, of ALL entries in that category - income
and spending both, not spending alone. Raise `ValueError` if the ledger
has no entries in that category.
