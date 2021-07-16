"""Example of binary search."""


def bsearch(data, value, i1=None, i2=None):
    """Returns the matching index for the passed in value.

    :param list data: The (sorted) list to lookup.
    :param value: The value to lookup.
    :param int i1: The index to start the search.
    :param int i2: The index to end the search.

    :return: The index of the matching item or None.
    :rtype: int | None
    """
    if not data:
        return None
    if i1 is None:
        i1 = 0
    if i2 is None:
        i2 = len(data) - 1

    index = (i2 - i1) // 2 + i1
    if data[index] == value:
        return index
    elif data[index] > value:
        return bsearch(data, value, i1, index - 1)
    else:
        return bsearch(data, value, index + 1, i2)


import random
import unittest


class TestBSearch(unittest.TestCase):
    """Tests the bsearch function."""

    def test_bsearch(self):
        """Tests the bsearch function."""
        for _ in range(1000):
            n = random.randint(1, 10)
            data = [random.randint(0, 10000) for _ in range(n)]
            data.sort()
            index = random.randint(0, len(data) - 1)
            value = data[index]
            self.assertEqual(index, bsearch(data, value))


if __name__ == '__main__':
    unittest.main()
