import unittest
from ledger.money import parse_amount
class G(unittest.TestCase):
    def test(self):
        for text, cents in [("12.5", 1250), ("12.05", 1205), ("12.50", 1250), ("$3.99", 399), ("7", 700), (" 0.1 ", 10)]:
            self.assertEqual(parse_amount(text), cents, text)
        with self.assertRaises(ValueError):
            parse_amount("1.234")
if __name__ == "__main__": unittest.main()
