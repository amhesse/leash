import datetime, unittest
from ledger.store import Entry, Ledger
D = datetime.date
import pathlib
from ledger.budget import over_budget
class G(unittest.TestCase):
    def test(self):
        l = Ledger()
        for c, v in [("food", -300), ("food", -250), ("food", 100), ("rent", -1000), ("fun", -999)]:
            l.add(Entry(D(2026,1,1), c, v))
        self.assertEqual(over_budget(l, {"food": 500, "rent": 1000}), {"food": 50})
        self.assertEqual(over_budget(l, {"fun": 1}), {"fun": 998})
        self.assertEqual(over_budget(l, {}), {})
        self.assertEqual(over_budget(Ledger(), {"food": 0}), {})
    def test_has_test(self):
        self.assertIn("over_budget", pathlib.Path("tests/test_budget.py").read_text())
if __name__ == "__main__": unittest.main()
