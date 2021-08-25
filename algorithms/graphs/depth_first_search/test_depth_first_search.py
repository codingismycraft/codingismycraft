"""Test the dfs algorithm."""

import unittest

import depth_first_search as dfs


class TestDepthFirstSearch(unittest.TestCase):
    """Tests Depth First Search."""

    def test_dfs_example_1(self):
        """Tests the dfs example 2."""
        data = {
            '1': ['2', '3'],
            '2': ['1', '3'],
            '3': ['1', '2'],
        }

        dfs.dfs(data, '1')
        visited = dfs.dfs(data, '1')
        self.assertSetEqual(set(visited), set(data.keys()))

    def test_dfs_example_2(self):
        """Tests the dfs example 2."""
        data = {
            '1': ['2', '4'],
            '2': ['1', '3'],
            '3': ['1', '4'],
            '4': ['1', '3'],
        }

        visited = dfs.dfs(data, '1')
        self.assertSetEqual(set(visited), set(data.keys()))

    def test_dfs_example_3(self):
        """Tests the dfs example 2."""
        data = {
            '1': ['2', '4'],
            '2': ['1', '3', '4'],
            '3': ['1', '4'],
            '4': ['1', '3', '2'],
        }
        visited = dfs.dfs(data, '1')
        self.assertSetEqual(set(visited), set(data.keys()))

    def test_dfs(self):
        """Tests Depth First Search."""

        data = {
            '1': ['0', '2', '4', '3', '5'],
            '0': ['1', '3', '2'],
            '2': ['1', '0', '4'],
            '3': ['1', '0'],
            '4': ['1', '2'],
            '5': ['1']
        }

        print(dfs.dfs(data, '2'))

    def test_dfs_disconnected(self):
        """Tests Depth First Search."""

        data = {
            "A": ["C", "B", "D"],
            "B": ["A"],
            "C": ["A", "E"],
            "D": ["A", "E"],
            "E": ["C", "D"],
            "F": ["K"],
            "G": ["I", "H"],
            "H": ["G"],
            "I": ["G", "K"],
            "K": ["I", "F"],
            "L": []
        }

        retrieved, subgraph_count = dfs.dfs_disconnected(data)

        self.assertEqual(subgraph_count, 3)


if __name__ == '__main__':
    unittest.main()
