import unittest
from ledger.money import split_evenly, format_cents
class G(unittest.TestCase):
    def test(self):
        self.assertEqual(split_evenly(100, 3), [34, 33, 33])
        self.assertEqual(split_evenly(101, 3), [34, 34, 33])
        self.assertEqual(split_evenly(99, 3), [33, 33, 33])
        self.assertEqual(split_evenly(2, 5), [1, 1, 0, 0, 0])
        self.assertEqual(split_evenly(0, 2), [0, 0])
        self.assertEqual(split_evenly(7, 1), [7])
        for bad in (0, -1):
            with self.assertRaises(ValueError):
                split_evenly(10, bad)
        self.assertEqual(format_cents(1250), "$12.50")
if __name__ == "__main__": unittest.main()
