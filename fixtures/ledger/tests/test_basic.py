import datetime
import unittest

from ledger.money import format_cents
from ledger.report import summary
from ledger.store import Entry, Ledger


class Basic(unittest.TestCase):
    def test_format(self):
        self.assertEqual(format_cents(1250), "$12.50")

    def test_summary(self):
        ledger = Ledger()
        ledger.add(Entry(datetime.date(2026, 1, 1), "food", 1000))
        ledger.add(Entry(datetime.date(2026, 1, 2), "pay", 5000))
        self.assertIn("balance: $60.00", summary(ledger))
