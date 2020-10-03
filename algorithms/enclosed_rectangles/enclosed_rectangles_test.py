"""Tests the enclosed rectangles solution."""

import unittest

import enclosed_rectangles


class EnclosedRectanglesTest(unittest.TestCase):
    """Tests the enclosed rectangles solution."""

    def test_count_rectangles(self):
        """Tests the count_rectangles function."""
        test_values = {2: 1, 3: 9, 4: 36, 5: 100}

        for n, expected in test_values.items():
            retrived = enclosed_rectangles.count_rectangles(n)
            self.assertEqual(expected, retrived)

if __name__ == '__main__':
    unittest.main()