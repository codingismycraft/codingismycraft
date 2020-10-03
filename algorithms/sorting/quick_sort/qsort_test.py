"""Tests the quick sort algorithm."""

import unittest
import random
import qsort

# Aliases.
partition = qsort.partition
qsort = qsort.qsort


class TestPartition(unittest.TestCase):
    """Tests the partition function."""

    def test_empty_list(self):
        """Test empty list."""
        i = []
        self.assertEqual(partition(i, 0, 0), 0)

    def test_one_element(self):
        """Test one element array."""
        i = [1]
        self.assertEqual(partition(i, 0, len(i) - 1), 0)

    def test_two_elements(self):
        """Test two elements array."""
        data = [9, 1]
        partition(data, 0, len(data) - 1)
        self.assertListEqual(data, [1, 9])

    def test_same_elements(self):
        """Test one element array."""
        data = [3, 3, 3]
        partition(data, 0, 2)
        self.assertListEqual(data, sorted(data))

    def test_sort(self):
        """Tests sorting for random arrays."""
        for l in range(random.randint(0, 100)):
            data = [random.randint(0, 100000) for _ in range(l)]
            qsort(data)
            self.assertListEqual(data, sorted(data))


if __name__ == '__main__':
    unittest.TestCase()
