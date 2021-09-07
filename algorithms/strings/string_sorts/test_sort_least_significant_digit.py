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



if __name__ == '__main__':
    unittest.main()
