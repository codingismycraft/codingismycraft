"""Tests remove_islands.

See also: https://www.youtube.com/watch?v=4tYoVx0QoN0
"""

import unittest

import remove_islands


class TestRemoveIslands(unittest.TestCase):
    """Tests the solution to the remove islands problem."""

    def test_remove_islands(self):
        """Test remove islands."""

        input = [
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 1, 1],
            [0, 0, 1, 0, 1, 0],
            [1, 1, 0, 0, 1, 0],
            [1, 0, 1, 1, 0, 0],
            [1, 0, 0, 0, 0, 1]
        ]

        expected = [
            [1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 1, 0],
            [1, 1, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 1]
        ]

        retrieved = remove_islands.remove_islands(input)

        for row1, row2 in zip(expected, retrieved):
            self.assertListEqual(row1, row2)


if __name__ == '__main__':
    unittest.main()
