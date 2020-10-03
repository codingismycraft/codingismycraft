""""Tests the max_area module."""

import unittest

import max_area

# Aliases.
Point = max_area.Point
get_max_area = max_area.get_max_area


class MaxAreaTest(unittest.TestCase):
    """"Tests the max_area module."""

    def test_get_max_area(self):
        """Tests the get_max_area function."""
        points = [Point(1, 3), Point(2, 5), Point(5, 1), Point(8, 5)]
        expected = 30
        retrieved = get_max_area(points)
        self.assertEqual(expected, retrieved)

        points = [Point(1, 135), Point(2, 135), Point(5, 35), Point(8, 5)]
        expected = 140
        retrieved = get_max_area(points)
        self.assertEqual(expected, retrieved)

        points = [Point(1, 135), Point(2, 135), Point(5, 5), Point(8, 5)]
        expected = 135
        retrieved = get_max_area(points)
        self.assertEqual(expected, retrieved)


if __name__ == '__main__':
    unittest.TestCase()
