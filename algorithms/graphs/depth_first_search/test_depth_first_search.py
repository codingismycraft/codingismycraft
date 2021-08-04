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

        visited, path, all_steps = dfs.dfs(data, '1')
        self.assertSetEqual(set(visited), set(data.keys()))
        print('path:      ', path)
        print('all_steps: ', all_steps)

    def test_dfs_example_2(self):
        """Tests the dfs example 2."""
        data = {
            '1': ['2', '4'],
            '2': ['1', '3'],
            '3': ['1', '4'],
            '4': ['1', '3'],
        }

        visited, path, all_steps = dfs.dfs(data, '1')
        self.assertSetEqual(set(visited), set(data.keys()))
        print('path:      ', path)
        print('all_steps: ', all_steps)

    def test_dfs_example_3(self):
        """Tests the dfs example 2."""
        data = {
            '1': ['2', '4'],
            '2': ['1', '3', '4'],
            '3': ['1', '4'],
            '4': ['1', '3', '2'],
        }

        visited, path, all_steps = dfs.dfs(data, '1')
        self.assertSetEqual(set(visited), set(data.keys()))
        print('path:      ', path)
        print('all_steps: ', all_steps)

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

        visited, path, all_steps = dfs.dfs(data, '2')
        #self.assertSetEqual(set(visited), set(data.keys()))
        print('path:      ', path)
        print('all_steps: ', all_steps)


if __name__ == '__main__':
    unittest.main()
