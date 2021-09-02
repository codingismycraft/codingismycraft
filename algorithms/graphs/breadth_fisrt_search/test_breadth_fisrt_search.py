"""Test the bfs algorithm."""

import unittest

import breadth_fisrt_search as bfs



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
        expected = ['5', '7', '8']
        retrieved = bfs.bsf(data, '5', '8')
        print(retrieved)
        self.assertListEqual(expected, retrieved)

    def test_bsf_example_1(self):
        """Tests example 1."""
        data = {
            '1': ['2', '3'],
            '2': ['1', '4'],
            '3': ['1', '4'],
            '4': ['2', '5'],
            '5': ['4'],
            '6': ['2', '4']
        }
        expected = ['1', '2', '4', '5']
        retrieved = bfs.bsf(data, '1', '5')
        self.assertListEqual(expected, retrieved)



if __name__ == '__main__':
    unittest.main()
