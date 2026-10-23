TDD: first write a new test file, `tests/test_budget.py`, with unit tests
for `over_budget`; then create `ledger/budget.py` so those tests pass.
The function `over_budget(ledger, limits: dict[str, int]) -> dict[str, int]`
takes a `ledger.store.Ledger` and a mapping of category to spending limit
in positive cents. Spending is the negated sum of negative entries in a
category. Return a mapping of each category whose spending exceeds its
limit to the amount over, in cents. Categories without a limit are
ignored. The test file does not exist yet; writing it is part of the
task.
