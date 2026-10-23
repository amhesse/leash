import unittest
from ledger.money import parse_amount
class G(unittest.TestCase):
    def test(self):
        for text, cents in [("-12.50", -1250), ("-12", -1200), ("12.50", 1250),
                            ("-0.50", -50), ("$3.99", 399)]:
            self.assertEqual(parse_amount(text), cents, text)
if __name__ == "__main__": unittest.main()
