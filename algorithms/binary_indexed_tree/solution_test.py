"""Tests the solution to running_count."""

import random
import unittest

import solution


class SolutionTest(unittest.TestCase):
    """Tests the solution to running_count."""

    def test_brutal_solution(self):
        """Tests the brutal solution."""
        length = 10
        values = [random.randint(1, 50) for _ in range(length)]
        rc = solution.BrutalRunningCount(values)
        for i in range(0, length):
            self.assertEqual(sum(values[0:i + 1]), rc.get_total(i))
        values[4] += 6
        rc.increase(4, 6)
        for i in range(0, length):
            self.assertEqual(sum(values[0:i + 1]), rc.get_total(i))

    def test_construction(self):
        """Tests the construction of the running count.

        Uses pre calculated values to test the creation of the sum graph
        (see the documentation for details about how these values are
        created and what they mean).

        Also tests the method to increase a value stored in an particular
        index and also the method to retrieve sums.
        """
        values = [2, 8, 3, 6, 1, 2, 5, 1, 9, 7, 2, 8, 8, 5, 1]
        expected = [0, 2, 10, 3, 19, 1, 3, 5, 28, 9, 16, 2, 26, 8, 13, 1]
        rc = solution.RunningCount(values)
        self.assertListEqual(rc._running_count, expected)
        for i in range(0, len(values)):
            expected = sum(values[0:i + 1])
            self.assertEqual(expected, rc.get_total(i))
        index = 4
        value = 6
        rc.increase(index, value)
        values[index] += value
        for i in range(0, len(values)):
            self.assertEqual(sum(values[0:i + 1]), rc.get_total(i))


if __name__ == '__main__':
    unittest.main()
