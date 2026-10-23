TDD: implement `ledger/budget.py` so `tests/test_budget.py` passes: a
function `over_budget(ledger, limits: dict[str, int]) -> dict[str, int]`
takes a `ledger.store.Ledger` and a mapping of category to spending limit
in positive cents. Spending is the negated sum of negative entries in a
category. Return a mapping of each category whose spending exceeds its
limit to the amount over, in cents. Categories without a limit are
ignored.
