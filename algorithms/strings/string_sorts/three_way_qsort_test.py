"""Tests three way sorting."""

import unittest

import three_way_qsort


class TestThreeWaySort(unittest.TestCase):
    """Tests three way sorting."""

    def test_three_way_qsort(self):
        data = [
            'dda',
            'adb  ',
            'acc',
            'zab   ',
            'zab   ',
            'zxy',
            'zaasas',
            'bad',
            'aaaab ',
            'aaak',
            'aaaabcddd',
            'bae',
            'zxy',
            'acc',
            'acc',
        ]

        strings = data[:]
        three_way_qsort.three_way_sort(strings)
        expected = sorted(strings)
        self.assertListEqual(expected, strings)


if __name__ == '__main__':
    unittest.main()
