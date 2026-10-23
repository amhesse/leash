In `ledger/money.py`, add a function `split_evenly_signed(cents: int, parts: int) -> list[int]`
that splits `cents` - which may be positive, negative, or zero - into
`parts` integers that sum exactly to `cents`, where every result differs
from every other by at most 1 in absolute value, and the amounts with
the larger absolute value come first. All results must have the same
sign as `cents` (or be 0, when `cents` is 0). `parts` less than 1 raises
`ValueError`. Example: `split_evenly_signed(-100, 3)` returns
`[-34, -33, -33]`. Do not change `parse_amount` or `format_cents`.
