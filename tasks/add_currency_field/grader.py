import contextlib, io, os, tempfile, unittest
from ledger.store import Entry
from ledger import cli


def run(csv_text):
    with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False) as f:
        f.write(csv_text)
    try:
        return cli.load(f.name)
    finally:
        os.unlink(f.name)


class G(unittest.TestCase):
    def test_default(self):
        self.assertEqual(Entry.__dataclass_fields__["currency"].default, "USD")

    def test_3_columns(self):
        ledger = run("2026-01-01,food,-10\n")
        self.assertEqual(ledger.entries[0].note, "")
        self.assertEqual(ledger.entries[0].currency, "USD")

    def test_4_columns_note_unchanged(self):
        ledger = run("2026-01-01,food,-10,lunch\n")
        self.assertEqual(ledger.entries[0].note, "lunch")
        self.assertEqual(ledger.entries[0].currency, "USD")

    def test_5_columns_currency(self):
        ledger = run("2026-01-01,food,-10,lunch,EUR\n")
        self.assertEqual(ledger.entries[0].note, "lunch")
        self.assertEqual(ledger.entries[0].currency, "EUR")

    def test_cli_still_runs(self):
        out = io.StringIO()
        with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False) as f:
            f.write("2026-01-01,food,-10,,GBP\n2026-01-02,pay,50\n")
        try:
            with contextlib.redirect_stdout(out):
                cli.main([f.name])
        finally:
            os.unlink(f.name)
        self.assertIn("balance: $40.00", out.getvalue())


if __name__ == "__main__": unittest.main()
