import unittest

import heap_impl


class TestHeap(unittest.TestCase):
    def test_push(self):
        heap = []
        input = [120, 10, 5, 150, 1, 3]
        for i in input:
            heap_impl.push(heap, i)
        expected_heap = [1, 5, 3, 150, 120, 10]
        self.assertListEqual(heap, expected_heap)

    def test_pop(self):
        heap = []
        input = [120, 10, 5, 150, 7, 1, 3]
        for i in input:
            heap_impl.push(heap, i)
        sorted_list = []
        v = heap_impl.pop(heap)
        while v is not None:
            sorted_list.append(v)
            v = heap_impl.pop(heap)
        expected = sorted(input)
        self.assertListEqual(expected, sorted_list)


if __name__ == "__main__":
    unittest.main()
