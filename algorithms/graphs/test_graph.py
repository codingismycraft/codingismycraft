"""Test the graph module."""

import unittest

import graph

# Aliases.
Graph = graph.Graph


class TestGraph(unittest.TestCase):
    """Tests the graph class."""

    def test_graph_population(self):
        """Tests populating graph."""
        data = {
            'a': ['b', 'c'],
            'b': ['c', 'a'],
            'c': ['b', 'a']
        }

        g = Graph()
        for k, v in data.items():
            g.add_node(k)
            for n in v:
                g.add_edge(k, n)

        for k, v in data.items():
            self.assertListEqual(sorted(list(g.get_edges(k))), sorted(v))


if __name__ == '__main__':
    unittest.main()
