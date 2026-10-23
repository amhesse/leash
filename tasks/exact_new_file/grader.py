import unittest, pathlib
EXPECTED = '"""Shared constants."""\n\nDEFAULT_CURRENCY = "USD"\nCENTS_PER_UNIT = 100\n'
class G(unittest.TestCase):
    def test(self):
        self.assertEqual(pathlib.Path("ledger/constants.py").read_text(), EXPECTED)
if __name__ == "__main__": unittest.main()
