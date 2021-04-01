"""Implements a max heap."""

import unittest

def get_parent_index(index):
    if index <= 0:
        return -1

    if index % 2 == 0:
        index -= 1

    return index // 2


def get_children(index):
    left = index * 2 + 1
    right = left + 1
    return left, right


def push(heap, value):
    # Add to the end of the heap
    heap.append(value)
    move_upward(heap, len(heap) - 1)


def pop(heap):
    if len(heap) == 0:
        return None
    value = heap.pop(0)
    if len(heap) == 0:
        return value
    last_value = heap.pop()
    heap.insert(0, last_value)
    move_down(heap, 0)
    return value


def move_down(heap, index):
    left, right = get_children(index)

    if left >= len(heap) and right >= len(heap):
        # Reached end of heap.
        return

    if right >= len(heap):
        # There should only be a left child.
        index_to_check = left
    else:
        if heap[left] >= heap[right]:
            index_to_check = left
        else:
            index_to_check = right

    if heap[index] >= heap[index_to_check]:
        # Nothing to do.
        return
    else:
        # Move larger child up and move the switched value down.
        swap(heap, index_to_check, index)
        move_down(heap, index_to_check)


def move_upward(heap, index):
    parent = get_parent_index(index)
    if parent >= 0 and heap[parent] < heap[index]:
        swap(heap, parent, index)
        move_upward(heap, parent)


def swap(heap, i1, i2):
    heap[i1], heap[i2] = heap[i2], heap[i1]


class HeapTest(unittest.TestCase):

    def test_heap(self):
        a = [1, 9, 2, 8]
        heap = []
        for v in a:
            push(heap, v)
        b = []
        v = pop(heap)
        while v is not None:
            b.append(v)
            v = pop(heap)
        expected = sorted(a)
        expected.reverse()
        self.assertListEqual(expected, b)


if __name__ == '__main__':
    unittest.main()
