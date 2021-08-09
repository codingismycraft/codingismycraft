"""Tests the kruskal module."""

import unittest

import kruskal


class TestKruskal(unittest.TestCase):
    """Tests the kruskal function."""

    def test_kruskal_example_1(self):
        """Tests the kruskal function using example 1 data."""
        data = {
            '1': [('2', 6), ('3', 1)],
            '2': [('1', 6), ('3', 5), ('4', 7), ('6', 3)],
            '3': [('1', 1), ('2', 5), ('4', 6)],
            '4': [('2', 7), ('3', 6), ('5', 8), ('6', 2)],
            '5': [('4', 8)],
            '6': [('2', 3), ('4', 2)],
        }
        expected_weight = 19

        path, retrieved_weight = kruskal.kruskal(data)
        self.assertEqual(retrieved_weight, expected_weight)

    def test_kruskal_example_2(self):
        """Tests the kruskal function using example 2 data."""
        data = {
            '1': [('6', 10), ('2', 28)],
            '2': [('1', 28), ('7', 14), ('3', 16)],
            '3': [('2', 16), ('4', 12)],
            '4': [('3', 12), ('7', 18), ('5', 22)],
            '5': [('4', 22), ('7', 24), ('6', 25)],
            '6': [('1', 10), ('5', 25)],
            '7': [('5', 24), ('4', 18), ('2', 14)],
        }
        expected_weight = 99
        path, retrieved_weight = kruskal.kruskal(data)
        self.assertEqual(retrieved_weight, expected_weight)


if __name__ == '__main__':
    unittest.main()
