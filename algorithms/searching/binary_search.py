"""Implements binary search."""

import math
import random
import unittest

MAX_INTEGER = 100000000

count = 0


class Data:
    def __init__(self, size):
        self.data = sorted(
            [random.randint(1, MAX_INTEGER) for _ in range(size)])

    def get_item_to_lookup(self):
        position = random.randint(0, len(self.data) - 1)
        return position, self.data[position]


def binary_search(array, value, start=None, end=None):
    global count
    count += 1

    assert isinstance(array, list)

    if start is None and end is None:
        start, end = 0, len(array) - 1

    if start > end:
        return None

    middle = ((end - start) // 2) + start

    if array[middle] == value:
        return middle

    if array[middle] < value:
        return binary_search(array, value, middle + 1, end)
    else:
        return binary_search(array, value, start, middle - 1)


def binary_search_iterative(array, value):
    assert isinstance(array, list)
    start, end = 0, len(array) - 1
    while start < end:
        middle = (end - start) // 2 + start
        if array[middle] == value:
            return middle
        elif array[middle] > value:
            end = middle - 1
        else:
            start = middle + 1
    else:
        assert start == end
        return start if array[start] == value else None


class BinarySearchTest(unittest.TestCase):

    def test_simple_cases(self):
        d = []
        self.assertEqual(binary_search(d, value=5), None)

        d = [1]
        self.assertEqual(binary_search(d, value=1), 0)
        self.assertEqual(binary_search(d, value=5), None)

        d = sorted([3, 8])
        self.assertEqual(binary_search(d, value=5), None)
        self.assertEqual(binary_search(d, value=3), 0)
        self.assertEqual(binary_search(d, value=8), 1)

    def test_random_data(self):
        global count
        for _ in range(10):
            d = Data(1000)
            p, v = d.get_item_to_lookup()
            count = 0
            self.assertEqual(binary_search(d.data, value=v), p)
            self.assertLess(count, 1 + math.log2(len(d.data)))

    def test_random_data_iterative(self):
        for _ in range(10):
            d = Data(10)
            p, v = d.get_item_to_lookup()
            self.assertEqual(binary_search_iterative(d.data, value=v), p)


if __name__ == '__main__':
    unittest.main()
