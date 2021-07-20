"""Test the bfs algorithm."""

import unittest

from .. import bfs
from .. import graph
from .. import utils

# Aliases.
Graph = graph.Graph


class TestGraph(unittest.TestCase):
    """Tests the graph class."""

    def test_bsf(self):
        """Tests BSF."""
        data = {
            '5': ['3', '7'],
            '3': ['2', '4'],
            '7': ['8', '5'],
            '2': [],
            '4': ['8'],
            '8': []
        }
        expected = [('8', '7'), ('7', '5')]
        g = Graph(data)
        retrieved = bfs.bsf(g, '5', '8')
        self.assertListEqual(expected, retrieved)
        utils.display_graph(g.get_as_dict(), retrieved)


if __name__ == '__main__':
    unittest.main()
