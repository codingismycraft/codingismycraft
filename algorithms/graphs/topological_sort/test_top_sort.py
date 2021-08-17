"""Test the top_sort module."""

import unittest

import top_sort


class TestTopSort(unittest.TestCase):
    """Tests the top_sort function."""

    def test_top_sort_1(self):
        """Tests the top_sort function."""
        data = {
            'A': ['B', 'C', 'D'],
            'B': ['E'],
            'C': ['F'],
            'D': ['F'],
            'E': [],
            'F': [],
        }

        retrieved = top_sort.top_sort(data)

        print(retrieved)

    def test_top_sort_2(self):
        """Tests the top_sort function."""
        data = {
            'A': ['C'],
            'B': ['C', 'D'],
            'C': ['E'],
            'D': ['F'],
            'E': ['H', 'F'],
            'F': ['G'],
            'H': [],
            'G': []
        }

        retrieved = top_sort.top_sort(data)

        print(retrieved)


if __name__ == '__main__':
    unittest.main()
