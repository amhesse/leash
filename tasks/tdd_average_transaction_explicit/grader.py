import datetime, pathlib, unittest
from ledger.store import Entry, Ledger
from ledger.stats import average_transaction
D = datetime.date
class G(unittest.TestCase):
    def test(self):
        l = Ledger()
        for c, v in [("food", -300), ("food", -250), ("food", 100), ("rent", -1000)]:
            l.add(Entry(D(2026, 1, 1), c, v))
        # mixed sign: (-300 - 250 + 100) / 3 = -150.0, not spending-only
        self.assertEqual(average_transaction(l, "food"), -150.0)
        self.assertEqual(average_transaction(l, "rent"), -1000.0)
        with self.assertRaises(ValueError):
            average_transaction(l, "fun")
        with self.assertRaises(ValueError):
            average_transaction(Ledger(), "food")
        l2 = Ledger()
        l2.add(Entry(D(2026, 1, 1), "x", 100))
        l2.add(Entry(D(2026, 1, 1), "x", 100))
        l2.add(Entry(D(2026, 1, 1), "x", 99))
        self.assertEqual(average_transaction(l2, "x"), 99.67)

    def test_has_test(self):
        self.assertIn("average_transaction", pathlib.Path("tests/test_stats.py").read_text())
if __name__ == "__main__": unittest.main()
