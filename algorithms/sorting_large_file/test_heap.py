"""Tests the Heap class."""

import unittest
import heap1 as heap

MaxHeap = heap.MaxHeap
MinHeap = heap.MinHeap


class TestHeap(unittest.TestCase):
    """Tests the Heap class."""

    def test_max_heap(self):
        """Tests the MaxHeap."""
        a = [20, 50, 100, 30, 8832, 1, 21, 3344, 11, 11, 20]
        heap = MaxHeap()
        for value in a:
            heap.add(value)
        self.assertEqual(len(heap), len(a))
        b = []
        v = heap.pop()
        while v is not None:
            b.append(v)
            v = heap.pop()
        sorted_a = sorted(a)
        sorted_a.reverse()
        self.assertListEqual(sorted_a, b)

    def test_min_heap(self):
        """Tests the MinHeap."""
        a = [20, 50, 100, 30, 8832, 1, 21, 3344, 11, 11, 20]
        heap = MinHeap()
        for value in a:
            heap.add(value)
        self.assertEqual(len(heap), len(a))
        b = []
        v = heap.pop()
        while v is not None:
            b.append(v)
            v = heap.pop()
        sorted_a = sorted(a)
        self.assertListEqual(sorted_a, b)


if __name__ == '__main__':
    unittest.main()
