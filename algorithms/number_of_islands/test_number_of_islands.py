"""Tests the number_of_islands solution."""

import unittest

import number_of_islands
import max_area_of_island


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


    def test_max_area(self):
        """Tests max_area solution."""
        input = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
         [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

        expected = 6

        solution = max_area_of_island.Solution()

        self.assertEqual(solution.maxAreaOfIsland(input), expected)


if __name__ == '__main__':
    unittest.main()
