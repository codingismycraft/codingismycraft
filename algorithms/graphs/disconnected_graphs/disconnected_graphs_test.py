"""Tests the disconnected_graphs module."""

import unittest

import disconnected_graphs


class TestDisconnectedGraphs(unittest.TestCase):
    """Tests the find_disconnected_graphs function."""

    def test_make_weakly_connected_graph(self):
        """Tests the make_weakly_connected."""
        data = {
            "A": ["B", "C", "D"],
            "B": [],
            "C": ["E"],
            "D": ["E"],
            "E": [],
        }

        print(disconnected_graphs.make_weakly_connected_graph(data))

    def test_find_disconnected_graphs(self):
        """Tests the find_disconnected_graphs function."""
        data = {
            "A": ["B", "C", "D"],
            "B": [],
            "C": ["E"],
            "D": ["E"],
            "E": [],
            "F": ["K"],
            "G": ["H", "I"],
            "H": [],
            "I": ["K"],
            "K": [],
            "L": []
        }
        retrieved = disconnected_graphs.find_disconnected_graphs(
            data
        )

        self.assertEqual(len(retrieved), 3)

        del data["L"]

        retrieved = disconnected_graphs.find_disconnected_graphs(
            data
        )
        self.assertEqual(len(retrieved), 2)

    def test_find_disconnected_graphs2(self):
        """Tests the find_disconnected_graphs function."""
        data = {
            "A": ["B", "C", "D"],
            "B": [],
            "C": ["E"],
            "D": ["E"],
            "E": [],
            "F": ["K"],
            "G": ["H", "I", "K"],
        }

        retrieved = disconnected_graphs.find_disconnected_graphs(
            data
        )
        self.assertEqual(len(retrieved), 2)


if __name__ == '__main__':
    unittest.main()
