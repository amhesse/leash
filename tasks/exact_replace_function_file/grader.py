import unittest
from ledger.money import format_cents
class G(unittest.TestCase):
    def test(self):
        self.assertEqual(format_cents(-150), "-$1.50")
        self.assertEqual(format_cents(1250), "$12.50")
if __name__ == "__main__": unittest.main()
