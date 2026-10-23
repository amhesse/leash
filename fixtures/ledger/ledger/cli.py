"""ledger CLI: reads a CSV of date,category,amount,note and prints a summary."""

import argparse
import csv
import datetime

from .money import parse_amount
from .report import summary
from .store import Entry, Ledger


def load(path: str) -> Ledger:
    ledger = Ledger()
    with open(path, newline="") as f:
        for row in csv.reader(f):
            date, category, amount = row[0], row[1], row[2]
            note = row[3] if len(row) > 3 else ""
            ledger.add(Entry(datetime.date.fromisoformat(date), category,
                             parse_amount(amount), note))
    return ledger


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="ledger")
    parser.add_argument("csv")
    args = parser.parse_args(argv)
    print(summary(load(args.csv)))
    return 0
