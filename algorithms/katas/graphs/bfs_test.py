import unittest

import bfs

GRAPH = {
    '1': ['3', '2'],
    '2': ['1', '4', '6'],
    '3': ['1', '4'],
    '4': ['3', '2', '6', '5'],
    '5': ['4'],
    '6': ['2', '4'],
}


class TestBfs(unittest.TestCase):
    def test_bfs(self):
        retrieved = bfs.find_shortest_path(GRAPH, '1', '5')
        expected = ['1', '3', '4', '5']
        self.assertListEqual(expected, retrieved)

        retrieved = bfs.find_shortest_path(GRAPH, '6', '2')
        expected = ['6', '2']
        self.assertListEqual(expected, retrieved)

        retrieved = bfs.find_shortest_path(GRAPH, '2', '5')
        expected = ['2', '4', '5']
        self.assertListEqual(expected, retrieved)


if __name__ == '__main__':
    unittest.main()