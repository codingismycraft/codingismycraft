"""Tests the key_indexed module."""

import datetime
import faker
import pickle
import random
import unittest

import key_indexed
import utils

# Alias.
key_indexed_sort = key_indexed.key_indexed_sort


def get_sorted_data(data):
    """Used for testing purposes to compute the expected sorted strings.

    :param list[Tuple[str, int]] data: A list of tuples consisting of a string
    and a section to sort by.

    :returns: A list of string sorted by sector.
    :rtype: List[str]
    """
    data = sorted(data, key=lambda d: d[1])
    return [d[0] for d in data]


class TestKeyIndexed(unittest.TestCase):
    """Test the key_indexed module."""

    def test_key_indexed_sort(self):
        """Tests the sort function."""
        data = [
            ('Christian Long', 2),
            ('Brittney Ayala', 3),
            ('Eric Macias', 2),
            ('Lindsey Harvey', 3),
            ('Sandra Sanders', 2),
            ('Mr. Timothy Young', 2),
            ('Chloe Huang', 1),
            ('Tonya Jones', 1),
            ('Erica Archer', 3),
            ('David Martinez', 3)
        ]

        retrieved = key_indexed_sort(data, 1, 3)
        self.assertListEqual(retrieved, get_sorted_data(data))

    def test_performance(self):
        """Compares the performance against a regular sort."""
        data = utils.read_data()

        t1 = datetime.datetime.now()
        retrieved = key_indexed_sort(data, 1, 30)
        t2 = datetime.datetime.now()
        key_indexed_sort_duration = (t2 - t1).total_seconds()

        t1 = datetime.datetime.now()
        expected = get_sorted_data(data)
        t2 = datetime.datetime.now()
        regular_sort_duration = (t2 - t1).total_seconds()

        self.assertListEqual(retrieved, expected)

        print(f'{len(retrieved)}, {len(expected)}')
        print(f'Regular sort duration: {regular_sort_duration} seconds')
        print(f'key indexed duration: {key_indexed_sort_duration} seconds')


if __name__ == '__main__':
    unittest.main()
