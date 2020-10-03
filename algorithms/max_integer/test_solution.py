"""Tests the effective solution."""

import unittest

import solution

data = [
    ["4321", 4, "1342"],
    ["100", 1, "010"],
    ["36789", 1000, "36789"],
    ["22", 22, "22"],
    ["9438957234785635408", 23, "0345989723478563548"],
]


class IndexTest(unittest.TestCase):
    """"Tests the index."""

    def test_creation(self):
        """Tests the index creation."""
        values = [2, 8, 3, 6, 1, 2, 5, 1, 9, 7, 2, 8, 8, 5, 1]
        expected = [0, 2, 10, 3, 19, 1, 3, 5, 28, 9, 16, 2, 26, 8, 13, 1]
        index = solution._Index(values)
        self.assertListEqual(expected, index._index)

    def test_get_sum(self):
        """Tests the index creation."""
        values = [2, 8, 3, 6, 1, 2, 5, 1, 9, 7, 2, 8, 8, 5, 1]
        index = solution._Index(values)

        for i in range(0, len(values)):
            expected = sum(values[0:i + 1])
            retrieved = index.get_sum(i)
            self.assertEqual(expected, retrieved)

    def test_increase(self):
        """Tests the increase method."""
        values = [2, 8, 3, 6, 1, 2, 5, 1, 9, 7, 2, 8, 8, 5, 1]
        index = solution._Index(values)
        i = 4
        increment = 1
        index.increase(i, increment)
        values[i] += increment
        for i in range(0, len(values)):
            expected = sum(values[0:i + 1])
            retrieved = index.get_sum(i)
            self.assertEqual(expected, retrieved)


class SolutionTest(unittest.TestCase):
    """Tests the solution to the min - integer problem."""

    def test_minInteger(self):
        """Tests the minInteger function."""
        for num, k, expected in data:
            num = list(num)
            retrieved = solution.minInteger(num, k)
            retrieved = ''.join(retrieved)
            self.assertEqual(retrieved, expected)

    def test_class(self):
        """Tests the class version."""
        for num, k, expected in data:
            s = solution.Solution()
            retrieved = s.minInteger(num, k)
            retrieved = ''.join(retrieved)
            self.assertEqual(retrieved, expected)


if __name__ == '__main__':
    unittest.main()
