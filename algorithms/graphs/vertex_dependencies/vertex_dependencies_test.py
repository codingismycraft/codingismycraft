"""Tests the vertex_dependencies module."""

import unittest

import vertex_dependencies

# Aliases.
DependencyCounter = vertex_dependencies.DependencyCounter

class TestVertexDependencies(unittest.TestCase):
    """Tests the vertex_dependencies module."""

    def test_count_dependencies(self):
        """Tests the make_weakly_connected."""
        data = {
            "A": ["B", "C", "D"],
            "B": [],
            "C": ["E"],
            "D": ["E"],
            "E": [],
            "F": ["K"],
            "G": ["H", "I"],
            "H": ["I"],
            "I": ["K"],
            "K": [],
            "L": []
        }

        expected = {
            "A": 4,
            "B": 0,
            "C": 1,
            "D": 1,
            "E": 0,
            "F": 1,
            "G": 3,
            "I": 1,
            "H": 2,
            "K": 0,
            "L": 0
        }

        retrieved = DependencyCounter.count_dependencies(data)

        self.assertEqual(len(retrieved), len(expected))

        for k, v in retrieved.items():
            self.assertEqual(v, expected[k])

    def test_count_dependencies2(self):
        """Tests the make_weakly_connected."""
        data = {
            "1": ["2", "3"],
            "2": ["6"],
            "3": ["4"],
            "4": ["5"],
            "5": ["6"],
            "6": []
        }

        expected = {
            "1": 5,
            "2": 1,
            "3": 3,
            "4": 2,
            "5": 1,
            "6": 0
        }

        retrieved = DependencyCounter.count_dependencies(data)

        self.assertEqual(len(retrieved), len(expected))

        for k, v in retrieved.items():
            self.assertEqual(v, expected[k])


if __name__ == '__main__':
    unittest.main()
