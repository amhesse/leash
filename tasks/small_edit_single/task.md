In `ledger/money.py`, change `format_cents` so negative amounts render
with the minus sign before the dollar sign: -150 becomes "-$1.50", not
"$-2.50". Positive output must not change. Do not change `parse_amount`.
