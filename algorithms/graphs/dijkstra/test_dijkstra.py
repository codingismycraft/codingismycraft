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
            "C": [("A", 7), ("B", 1), ("D", 18), ("E", 1)],
            "D": [("C", 18), ("B", 20), ("E", 1)],
            "E": [("C", 1), ("D", 1)]
        }

        retrieved = dijkstra.evaluate(graph, "A")

        print(retrieved)


if __name__ == '__main__':
    unittest.main()
