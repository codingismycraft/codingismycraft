"""Test the dfs algorithm."""

import unittest

from .. import depth_first_search as dfs
from .. import graph

# Aliases.
Graph = graph.Graph


class TestDepthFirstSearch(unittest.TestCase):
    """Tests Depth First Search."""

    def test_dfs(self):
        """Tests Depth First Search."""

        data = {
            '1': ['2', '0', '4', '3', '5'],
            '0': ['1', '3', '2'],
            '2': ['1', '0', '4', '2'],
            '3': ['1', '0'],
            '4': ['1', '2'],
            '5': ['1']
        }

        g = Graph(data)
        visited, path = dfs.dfs(g.get_as_dict(), '2')
        print(visited)
        print(path)
        self.assertSetEqual(set(visited), set(data.keys()))

    def test_find_path(self):
        """Tests Depth First Search."""
        data = {
            '0': ['1', '2', '3'],
            '1': ['0', '3', '4', '2', '5'],
            '2': ['0', '2', '1'],
            '3': ['1', '0'],
            '4': ['2', '1'],
            '5': ['1']
        }

        g = Graph(data)
        _, path = dfs.dfs(g.get_as_dict(), '2', '5')
        print(path)


if __name__ == '__main__':
    unittest.main()
