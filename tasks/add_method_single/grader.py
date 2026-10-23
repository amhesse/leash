import datetime, unittest
from ledger.store import Entry, Ledger
D = datetime.date
class G(unittest.TestCase):
    def test(self):
        l = Ledger()
        self.assertEqual(l.total_for("food"), 0)
        l.add(Entry(D(2026,1,1), "food", -300)); l.add(Entry(D(2026,1,2), "food", -200))
        l.add(Entry(D(2026,1,3), "pay", 900))
        self.assertEqual(l.total_for("food"), -500)
        self.assertEqual(l.total_for("pay"), 900)
        self.assertEqual(l.balance(), 400)
if __name__ == "__main__": unittest.main()
