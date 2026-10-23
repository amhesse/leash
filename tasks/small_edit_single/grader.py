import unittest
from ledger.money import format_cents, parse_amount
class G(unittest.TestCase):
    def test(self):
        self.assertEqual(format_cents(-150), "-$1.50")
        self.assertEqual(format_cents(-5), "-$0.05")
        self.assertEqual(format_cents(0), "$0.00")
        self.assertEqual(format_cents(1250), "$12.50")
    def test_parse_untouched(self):
        self.assertEqual(parse_amount("12.5"), 1205)  # the planted bug must still be there
if __name__ == "__main__": unittest.main()
