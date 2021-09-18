"""Tests sorting by most significant digit."""

import unittest

import sort_msd


class TestSortingByMSD(unittest.TestCase):
    """Tests sorting by most significant digit."""

    def test_count_frequencies(self):
        data = [
            'dda',
            'adb  ',
            'acc',
            'zab   ',
            'zaasas',
            'bad',
            'aaaab ',
            'aaak',
            'aaaabcddd',
            'bae',
        ]
        strings = data[:]
        sort_msd.msd_sort(strings)
        expected = sorted(data)
        self.assertListEqual(expected, strings)


if __name__ == '__main__':
    unittest.main()
