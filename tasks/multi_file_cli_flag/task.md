Add a `--category NAME` option to the ledger CLI so only entries in that
category are summarised. Add `Ledger.filtered(category: str) -> Ledger`
in `ledger/store.py` returning a new Ledger containing only matching
entries (the original is unchanged), and use it from `main` in
`ledger/cli.py` when the option is given. Without the option, output
must not change.
