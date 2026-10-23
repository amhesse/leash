Fix a bug in `ledger/money.py`: `parse_amount("12.5")` returns 1205 but
should return 1250. "12.05" must still return 1205, and "$3.99" must
return 399. A fractional part with more than two digits should raise
`ValueError`.
