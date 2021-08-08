"""Tests the number_of_islands solution."""

import unittest

import number_of_islands
import use_adj_matrix


class TestNumberOfIslands(unittest.TestCase):
    """Tests the number_of_islands solution."""

    def test_number_of_islands_1(self):
        """Tests the number_of_islands function."""
        matrix = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
        expected = 1

        solution = number_of_islands.Solution()
        retrieved = solution.numIslands(matrix)

        self.assertEqual(expected, retrieved)

        solution = use_adj_matrix.Solution()
        retrieved = solution.numIslands(matrix)

        self.assertEqual(expected, retrieved)

    def test_number_of_islands_2(self):
        """Tests the number_of_islands function."""
        matrix = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        expected = 3

        # solution = number_of_islands.Solution()
        # retrieved = solution.numIslands(matrix)
        #
        # self.assertEqual(expected, retrieved)

        solution = use_adj_matrix.Solution()
        retrieved = solution.numIslands(matrix)

        self.assertEqual(expected, retrieved)


if __name__ == '__main__':
    unittest.main()
