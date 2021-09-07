"""Tests the key_indexed module."""

import datetime
import unittest

import sort_key_indexed
import utils
import qsort

# Alias.
key_indexed_sort = sort_key_indexed.key_indexed_sort
qsort = qsort.qsort


class TestKeyIndexed(unittest.TestCase):
    """Test the key_indexed module."""

    def vefiry_solution(self, retrieved):
        """Verifies that the passed in data are sorted by sector."""
        self.assertTrue(retrieved)
        current_sector = retrieved[0][1]
        for _, sector in retrieved:
            self.assertTrue(sector >= current_sector)
            current_sector = sector

    def test_key_indexed_sort(self):
        """Tests the key index sort."""
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

        expected = [
            ('Chloe Huang', 1),
            ('Tonya Jones', 1),
            ('Christian Long', 2),
            ('Eric Macias', 2),
            ('Sandra Sanders', 2),
            ('Mr. Timothy Young', 2),
            ('Brittney Ayala', 3),
            ('Lindsey Harvey', 3),
            ('Erica Archer', 3),
            ('David Martinez', 3)
        ]

        retrieved = key_indexed_sort(data)
        self.assertListEqual(retrieved, expected)

    def test_performance(self):
        """Compares the performance against a regular sort."""
        data = utils.read_data(max_rows=1000)

        t1 = datetime.datetime.now()
        qsort(data, less_than=lambda obj1, obj2: obj1[1] < obj2[1])
        t2 = datetime.datetime.now()
        regular_sort_duration = (t2 - t1).total_seconds()
        print(f'Regular sort duration: {regular_sort_duration} seconds')

        data = utils.read_data(max_rows=1000)
        t1 = datetime.datetime.now()
        sorted_data = key_indexed_sort(data)
        t2 = datetime.datetime.now()
        key_indexed_sort_duration = (t2 - t1).total_seconds()
        print(f'key indexed duration: {key_indexed_sort_duration} seconds')
        faster_times = int(regular_sort_duration / key_indexed_sort_duration)
        print(f'Key sorting faster by {faster_times} times.')


if __name__ == '__main__':
    unittest.main()
