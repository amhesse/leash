import datetime, unittest, subprocess, sys, pathlib
from ledger.store import Entry, Ledger
class G(unittest.TestCase):
    def test(self):
        self.assertFalse(hasattr(Ledger, "add"))
        l = Ledger(); l.record(Entry(datetime.date(2026,1,1), "x", 5))
        self.assertEqual(l.balance(), 5)
        for p in ["ledger/cli.py", "tests/test_basic.py"]:
            self.assertNotIn(".add(", pathlib.Path(p).read_text(), p)
if __name__ == "__main__": unittest.main()
