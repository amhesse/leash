TDD: first write a new test file, `tests/test_stats.py`, with unit tests
for `average_transaction`; then create `ledger/stats.py` so those tests
pass. The function `average_transaction(ledger, category: str) -> float`
takes a `ledger.store.Ledger` and returns the average `cents` value, as a
float rounded to 2 decimal places, of ALL entries in that category -
income and spending both, not spending alone. Raise `ValueError` if the
ledger has no entries in that category. The test file does not exist
yet; writing it is part of the task.
