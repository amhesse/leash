import datetime
import unittest

from ledger.budget import over_budget
from ledger.store import Entry, Ledger


class Budget(unittest.TestCase):
    def test_over(self):
        ledger = Ledger()
        ledger.add(Entry(datetime.date(2026, 1, 1), "food", -600))
        self.assertEqual(over_budget(ledger, {"food": 500}), {"food": 100})
