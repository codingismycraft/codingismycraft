"""Tests the max integer solution."""

import unittest

import brutal_solution_1
import brutal_solution_2

data = [
    ["4321", 4, "1342"],
    ["100", 1, "010"],
    ["36789", 1000, "36789"],
    ["22", 22, "22"],
    ["9438957234785635408", 23, "0345989723478563548"],
]


class SolutionTest(unittest.TestCase):
    """Tests the solution to the min - integer problem."""

    def test_brutal_solution_1(self):
        """Tests the brutal solution."""
        for num, k, expected in data:
            retrieved = brutal_solution_1.minInteger(num, k)
            retrieved = ''.join(retrieved)
            self.assertEqual(retrieved, expected)

    def test_brutal_solution_2(self):
        """Tests the brutal solution."""
        for num, k, expected in data:
            retrieved = brutal_solution_2.minInteger(num, k)
            retrieved = ''.join(retrieved)
            self.assertEqual(retrieved, expected)

    def test_class(self):
        """Tests the brutal solution."""
        for num, k, expected in data:
            s = brutal_solution_1.Solution()
            retrieved = s.minInteger(num, k)
            retrieved = ''.join(retrieved)
            self.assertEqual(retrieved, expected)


if __name__ == '__main__':
    unittest.main()
