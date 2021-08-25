"""Tests the dijkstra module."""

import unittest

import dijkstra


class TestDijkstra(unittest.TestCase):
    """Tests the dijkstra module."""

    def test_evaluate(self):
        """Tests the evaluate function."""
        graph = {
            "A": [("B", 9), ("C", 7)],
            "B": [("A", 9), ("C", 1), ("D", 20)],
            "C": [("A", 7), ("B", 1), ("D", 18)],
            "D": [("C", 18), ("B", 20), ("E", 1)],
            "E": [("D", 1)]
        }

        retrieved = dijkstra.evaluate(graph, "A")
        expected = {'A': 0, 'B': 8, 'C': 7, 'D': 25, 'E': 26}
        print(retrieved)
        self.assertEqual(len(expected), len(retrieved))
        for key, value in retrieved.items():
            self.assertEqual(value, expected[key])


if __name__ == '__main__':
    unittest.main()
