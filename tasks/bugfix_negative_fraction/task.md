Fix a bug in `ledger/money.py`: `parse_amount("-12.50")` currently
returns -1150, but should return -1250 - a negative amount with a
fractional part is being miscalculated. `parse_amount("-12")` must
still return -1200, `parse_amount("12.50")` must still return 1250, and
`parse_amount("-0.50")` must return -50. Do not change `format_cents`
or `split_evenly`.
