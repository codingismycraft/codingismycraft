"""Tests the least significant sorting module."""

import datetime
import unittest

import sort_least_significant_digit
import utils
import qsort

# Alias.
lsd_sort = sort_least_significant_digit.lsd_sort
qsort = qsort.qsort


class TestLSDIndexed(unittest.TestCase):
    """Test the LSD sorting."""

    def vefiry_solution(self, retrieved):
        self.assertTrue(retrieved)
        current_sector = retrieved[0][1]
        for _, sector in retrieved:
            self.assertTrue(sector >= current_sector)
            current_sector = sector

    def test_lsd_sort(self):
        data = [
            "4PGC938",
            "2IYE230",
            "3CIO720",
            "1ICK750",
            "1OHV845",
            "4JZY524",
            "1ICK750",
            "3CIO720",
            "1OHV845",
            "1OHV845",
            "2RLA629",
            "2RLA629",
            "3ATW723",

        ]

        expected = [
            "1ICK750",
            "1ICK750",
            "1OHV845",
            "1OHV845",
            "1OHV845",
            "2IYE230",
            "2RLA629",
            "2RLA629",
            "3ATW723",
            "3CIO720",
            "3CIO720",
            "4JZY524",
            "4PGC938",
        ]

        retrieved = lsd_sort(data)
        self.assertListEqual(retrieved, expected)
        print(retrieved)

    def test_compare_with_quick_sort(self):
        """Compares LSG against quick sort."""
        MAX_ROWS = 3000
        data = utils.read_data(max_rows=MAX_ROWS)
        data = [d[0] for d in data]

        t1 = datetime.datetime.now()
        qsort(data)
        t2 = datetime.datetime.now()
        regular_sort_duration = (t2 - t1).total_seconds()
        print(f'Regular sort duration: {regular_sort_duration} seconds')

        data = utils.read_data(max_rows=MAX_ROWS)
        data = [d[0] for d in data]

        t1 = datetime.datetime.now()
        retrieved = lsd_sort(data)
        t2 = datetime.datetime.now()
        key_indexed_sort_duration = (t2 - t1).total_seconds()
        print(f'key indexed duration: {key_indexed_sort_duration} seconds')
        faster_times = int(regular_sort_duration / key_indexed_sort_duration)
        print(f'Key sorting faster by {faster_times} times.')


if __name__ == '__main__':
    unittest.main()
