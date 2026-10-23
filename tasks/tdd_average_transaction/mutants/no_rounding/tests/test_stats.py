import datetime
import unittest

from ledger.store import Entry, Ledger
from ledger.stats import average_transaction


class Stats(unittest.TestCase):
    def test_average_transaction(self):
        ledger = Ledger()
        ledger.add(Entry(datetime.date(2026, 1, 1), "food", -300))
        ledger.add(Entry(datetime.date(2026, 1, 2), "food", 100))
        self.assertEqual(average_transaction(ledger, "food"), -100.0)

    def test_average_transaction_missing_category(self):
        with self.assertRaises(ValueError):
            average_transaction(Ledger(), "nope")
