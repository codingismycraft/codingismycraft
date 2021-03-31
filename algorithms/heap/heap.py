""" Exposes the Heap class."""

import operator

import abc


class Heap(abc.ABC):
    """Encapsulates the details of a Heap class.

    :cvar list _heap: Holds the heap in its array representation.
    """

    def __init__(self):
        """Initializer."""
        self._heap = []

    def add(self, value):
        """Adds value in the heap.

        :param value: A value that supports comparisons.
        """
        self._heap.append(value)
        self._move_upwards_if_needed(len(self._heap) - 1)

    def pop(self):
        """Pops the fittest item from the heap.

        :return: The fittest item from the heap.
        """
        if len(self._heap) == 0:
            return None
        value = self._heap.pop(0)
        if len(self._heap) == 0:
            return value
        last_value = self._heap.pop()
        self._heap.insert(0, last_value)

        index = 0
        while True:
            left, right = self._find_children(index)

            if left >= len(self._heap) and right >= len(self._heap):
                return value

            if left < len(self._heap) <= right:
                if self._compare(self._heap[left], self._heap[index]):
                    self._swap(left, index)
                    index = left
                    continue
                else:
                    return value

            assert left < len(self._heap) and right < len(self._heap)

            if self._compare(self._heap[left], self._heap[right]):
                index_to_check = left
            else:
                index_to_check = right

            if self._compare(self._heap[index_to_check], self._heap[index]):
                self._swap(index_to_check, index)
                index = index_to_check
            else:
                return value

    def __len__(self):
        """Returns the length of the heap.

        :return: The length of the heap.
        :rtype: int
        """
        return len(self._heap)

    def _move_upwards_if_needed(self, index):
        """If needed switchs the value in the passed in index with its parent.

        :param int index: The index to process.
        """
        parent_index = self._find_parent(index)

        if parent_index >= 0:
            if self._compare(self._heap[index], self._heap[parent_index]):
                self._swap(parent_index, index)
                self._move_upwards_if_needed(parent_index)

    @classmethod
    def _find_children(cls, index):
        """Returns the children indexes.

        :param int index: The index to return the children indexes for.
        :rtype: tuple
        """
        left = index * 2 + 1
        right = 2 * (index + 1)
        return left, right

    @classmethod
    def _find_parent(cls, index):
        """Returns the parent index.

        :param int index: The index to return its parent.
        :rtype: int
        """
        if index <= 0:
            return -1
        elif index % 2 == 0:
            return index // 2 - 1
        else:
            return index // 2

    @abc.abstractmethod
    def _compare(self, v1, v2):
        """Compares two items.

        To be implemented in concrete classes.
        """

    def _swap(self, index1, index2):
        """Swaps the values for the passed in indexes.

        :param int index1: The left index to use.
        :param int index2: The right index to use.
        """
        self._heap[index1], self._heap[index2] = \
            self._heap[index2], self._heap[index1]


class MaxHeap(Heap):
    """Implements a MaxHeap."""

    def _compare(self, v1, v2):
        """Compares two items.

        :returns: True if v1 is greater or equal to v2.
        :rtype: bool
        """
        return operator.ge(v1, v2)


class MinHeap(Heap):
    """Implements a MinHeap."""

    def _compare(self, v1, v2):
        """Compares two items.

        :returns: True if v1 is less or equal to v2.
        :rtype: bool
        """
        return operator.le(v1, v2)

