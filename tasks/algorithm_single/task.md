In `ledger/money.py`, add a function `split_evenly(cents: int, parts: int) -> list[int]`
that splits an amount into `parts` integer amounts that sum exactly to
`cents`, differing from each other by at most 1 cent, with any larger
amounts first. `parts` less than 1 raises `ValueError`. Example:
`split_evenly(100, 3)` returns `[34, 33, 33]`. Do not change the existing
functions.
