"""Tests the efficient solution of the Buy-Sell stock problem."""

import random
import unittest

import buy_sell_stock

# Aliases.
left_side_max_deltas = buy_sell_stock.left_side_max_deltas
right_side_max_deltas = buy_sell_stock.right_side_max_deltas
get_max_profit = buy_sell_stock.get_max_profit


def brutal_find_max_delta(a):
    largest_so_far = None
    lower_so_far = None
    m = 0
    for v in reversed(a):
        if largest_so_far is None or largest_so_far < v:
            largest_so_far = v
            lower_so_far = v
        if lower_so_far is None or lower_so_far > v:
            lower_so_far = v
        m = max(m, largest_so_far - lower_so_far)
    return m


def brutal_solution(b):
    s = brutal_find_max_delta(b)
    for i in range(2, len(b) - 1):
        x1, x2 = b[0:i], b[i:]
        s = max(s, brutal_find_max_delta(x1) + brutal_find_max_delta(x2))
    return s


assert brutal_solution([3, 3, 5, 0, 0, 3, 1, 4]) == 6
assert brutal_solution([1, 2, 3, 4, 5]) == 4
assert brutal_solution([7, 6, 4, 3, 1]) == 0


class SolverTest(unittest.TestCase):
    """Tests the Solver class."""

    def creating_dummy_prices(self, n):
        """Creates a list or prices to use for stress testing.

        :param int n: The length of the list to create.

        :return: A list of prices.
        :rtype: list.
        """
        return [random.randint(0, 20) for _ in range(n)]

    def test_left_side_max_deltas(self):
        """Tests left_side_max_deltas."""
        testing_data = [
            [3, 3],
            [3, 5],
            [3, 3, 5],
            [3, 3, 5, 0, 0, 3, 1, 4],
            [7, 6, 4, 3, 1],
            [1, 2, 3, 4, 5],
        ]

        for data in testing_data:
            expected = []
            for i in range(1, len(data) + 1):
                expected.append(brutal_find_max_delta(data[0:i]))
            retrieved = left_side_max_deltas(data)
            self.assertEqual(len(retrieved), len(data))
            self.assertListEqual(retrieved, expected)

    def test_right_side_max_deltas(self):
        """Tests right_side_max_deltas."""
        testing_data = [
            [3, 3],
            [3, 5],
            [3, 3, 5],
            [3, 3, 5, 0, 0, 3, 1, 4],
            [7, 6, 4, 3, 1],
            [1, 2, 3, 4, 5],
            [1, 100, 100, 10, 80]
        ]

        for data in testing_data:
            expected = []
            i = len(data) - 1
            while i >= 0:
                expected.insert(0, brutal_find_max_delta(data[i:]))
                i -= 1
            retrieved = right_side_max_deltas(data)
            self.assertListEqual(retrieved, expected)

    def test_get_max_profit(self):
        """Tests the get_max_profit function."""
        self.assertEqual(get_max_profit([3, 3, 5, 0, 0, 3, 1, 4]), 6)
        self.assertEqual(get_max_profit([1, 2, 3, 4, 5]), 4)
        self.assertEqual(get_max_profit([7, 6, 4, 3, 1]), 0)

    def test_long_sequence(self):
        """Finds the timing for a long sequence of prices."""
        prices = self.creating_dummy_prices(1000)
        print(get_max_profit(prices))


if __name__ == '__main__':
    unittest.TestCase()
