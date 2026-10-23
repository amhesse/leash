import datetime, unittest
from ledger.store import Entry, Ledger
D = datetime.date
class G(unittest.TestCase):
    def test(self):
        l = Ledger()
        self.assertEqual(l.by_month(), {})
        l.add(Entry(D(2026,3,5), "a", 100)); l.add(Entry(D(2025,12,31), "a", -40))
        l.add(Entry(D(2026,3,1), "b", -10)); l.add(Entry(D(2026,1,9), "a", 5))
        got = l.by_month()
        self.assertEqual(got, {"2025-12": -40, "2026-01": 5, "2026-03": 90})
        self.assertEqual(list(got), ["2025-12", "2026-01", "2026-03"])
if __name__ == "__main__": unittest.main()
