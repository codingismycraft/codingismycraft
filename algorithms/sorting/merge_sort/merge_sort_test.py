"""Tests the merge sort module."""

import random
import unittest
import merge_sort

two_way_merge = merge_sort.two_way_merge
merge_sort = merge_sort.merge_sort


class MergeSortTest(unittest.TestCase):
    """Tests the merge sort module."""

    def test_two_way_merge_1(self):
        """Tests two_way_merge."""
        a1 = [
            random.randint(1, 1000)
            for _ in range(random.randint(1, 10000))
        ]
        a2 = [
            random.randint(1, 1000)
            for _ in range(random.randint(1, 10000))
        ]
        a1.sort()
        a2.sort()

        arr = a1 + a2
        temp = [None] * len(arr)
        two_way_merge(arr, 0, len(a1) - 1, len(arr) - 1, temp)
        expected = sorted(arr)
        self.assertListEqual(expected, arr)

    def test_two_way_merge_2(self):
        """Tests in_place_two_way_merge."""
        a = [7, 8, 9, 1, 2, 3]
        temp = [None] * len(a)
        two_way_merge(a, 0, 2, len(a) - 1, temp)
        self.assertListEqual(sorted(a), a)

    def test_merge_sort1(self):
        """Tests merge sort."""
        a = [7]
        temp = [None] * len(a)
        merge_sort(a, 0, len(a) - 1, temp)
        self.assertListEqual(sorted(a), a)

    def test_merge_sort2(self):
        a = [7, 6]
        merge_sort(a, 0, len(a)-1, a)
        self.assertListEqual(sorted(a), a)

    def test_merge_sort3(self):
        a = [7, 6, 1]
        merge_sort(a, 0, len(a) - 1)
        self.assertListEqual(sorted(a), a)

    def test_merge_sort4(self):
        """Tests two_way_merge."""
        for _ in range(10):
            a = [
                random.randint(1, 100)
                for _ in range(random.randint(1, 10000))
            ]
            merge_sort(a, 0, len(a) - 1)
            self.assertListEqual(sorted(a), a)


if __name__ == '__main__':
    unittest.TestCase()
