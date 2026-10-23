import datetime, unittest
from ledger.store import Entry, Ledger
D = datetime.date
import contextlib, io, os, tempfile
from ledger import cli
def run(*args):
    with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False) as f:
        f.write("2026-01-01,food,-10\n2026-01-02,pay,50\n2026-01-03,food,-2\n")
    out = io.StringIO()
    try:
        with contextlib.redirect_stdout(out):
            cli.main([f.name, *args])
    finally:
        os.unlink(f.name)
    return out.getvalue()
class G(unittest.TestCase):
    def test_filtered(self):
        l = Ledger(); l.add(Entry(D(2026,1,1), "a", 1)); l.add(Entry(D(2026,1,1), "b", 2))
        f = l.filtered("a")
        self.assertIsInstance(f, Ledger)
        self.assertEqual([e.category for e in f.entries], ["a"])
        self.assertEqual(len(l.entries), 2)
    def test_cli(self):
        self.assertEqual(run(), "food: $-12.00\npay: $50.00\nbalance: $38.00\n")
        got = run("--category", "pay")
        self.assertNotIn("food", got)
        self.assertIn("balance: $50.00", got)
if __name__ == "__main__": unittest.main()
