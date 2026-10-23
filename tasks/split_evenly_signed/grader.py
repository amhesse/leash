import unittest
from ledger.money import split_evenly_signed
class G(unittest.TestCase):
    def test(self):
        self.assertEqual(split_evenly_signed(-100, 3), [-34, -33, -33])
        self.assertEqual(split_evenly_signed(-101, 3), [-34, -34, -33])
        self.assertEqual(split_evenly_signed(100, 3), [34, 33, 33])
        self.assertEqual(split_evenly_signed(0, 3), [0, 0, 0])
        self.assertEqual(split_evenly_signed(-2, 5), [-1, -1, 0, 0, 0])
        self.assertEqual(split_evenly_signed(-7, 1), [-7])
        # sum, magnitude spread and sign are the real invariants - check
        # them directly rather than only the hand-picked examples above.
        for cents in (-100, -1, 0, 1, 100, -103, 103):
            for parts in (1, 2, 3, 7):
                result = split_evenly_signed(cents, parts)
                self.assertEqual(len(result), parts)
                self.assertEqual(sum(result), cents)
                mags = [abs(x) for x in result]
                self.assertEqual(mags, sorted(mags, reverse=True))
                self.assertLessEqual(max(mags) - min(mags), 1)
                self.assertTrue(all(x <= 0 for x in result) or all(x >= 0 for x in result))
        for bad in (0, -1):
            with self.assertRaises(ValueError):
                split_evenly_signed(10, bad)
if __name__ == "__main__": unittest.main()
