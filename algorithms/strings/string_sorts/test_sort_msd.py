"""Tests sorting by most significant digit."""

import unittest

import sort_msd


class TestSortingByMSD(unittest.TestCase):
    """Tests sorting by most significant digit."""

    def test_count_frequencies(self):
        data = [
            'kzy',
            'acb',
            'zzz',
            'bab',
            'lab',
            'aab',
        ]
        strings = data[:]
        sort_msd.msd_sort(strings, position=0, lo=0, hi=3)
        expected = [
            'kzy',
            'lab',
            'acb',
            'bbb',
        ]


    # def test1(self):
    #     data = [
    #         "b",
    #         "a",
    #     ]
    #     expected = ["a", "b"]
    #     retrieved = sort_msd.sort_by_msd(data, 1)
    #     self.assertListEqual(retrieved, expected)
    #     print(retrieved)
    #
    # def test2(self):
    #     data = [
    #         "ba",
    #         "aa",
    #     ]
    #     expected = ["aa", "ba"]
    #     retrieved = sort_msd.sort_by_msd(data, 2)
    #     self.assertListEqual(retrieved, expected)
    #     print(retrieved)

    # def test3(self):
    #     data = [
    #         "bc",
    #         "ba",
    #     ]
    #     expected = ["ba", "bc"]
    #     retrieved = sort_msd.sort_by_msd(data, 1)
    #     self.assertListEqual(retrieved, expected)
    #     print(retrieved)

    # def test4(self):
    #     data = [
    #         "bc",
    #         "ba",
    #     ]
    #     expected = ["ba", "bc"]
    #     retrieved = sort_msd.sort_by_msd(data, 1)
    #     self.assertListEqual(retrieved, expected)
    #     print(retrieved)


    def test_starting_positions(self):
        # data = [
        #     "acc",
        #     "klx",
        #     "abc",
        #     "kac",
        # ]
        return
        data = [
            "b",
            "a",
        ]
        char_index = 0
        retrieved = sort_msd.sort_by_msd(data)
        print(retrieved)


        # sorted_data = sorted(data)
        #
        # expected_positions = {}
        # for index, string in enumerate(sorted_data):
        #     c = ord(string[char_index])
        #     if c not in expected_positions:
        #         expected_positions[c] = index
        #
        # for c, p in expected_positions.items():
        #     print(chr(c), p)
        #     self.assertEqual(sorted_data[p][0], chr(c))
        #
        # print(sorted_data)

    # def test_sort_by_msd_1(self):
    #     """Tests the sort_by_msd fucntion."""
    #     data = [
    #         "abc",
    #         "klx",
    #         "acc",
    #     ]
    #     retrieved = sort_msd.sort_by_msd(data)
    #     expected = None
    #     self.assertEqual(retrieved, expected)
    #
    # def test_sort_by_msd(self):
    #     """Tests the sort_by_msd fucntion."""
    #     data = [
    #         "4PGC938",
    #         "2IYE230",
    #         "3CIO720",
    #         "1ICK750",
    #         "1OHV845",
    #         "4JZY524",
    #         "1ICK750",
    #         "3CIO720",
    #         "1OHV845",
    #         "1OHV845",
    #         "2RLA629",
    #         "2RLA629",
    #         "3ATW723",
    #
    #     ]
    #
    #     expected = [
    #         "1ICK750",
    #         "1ICK750",
    #         "1OHV845",
    #         "1OHV845",
    #         "1OHV845",
    #         "2IYE230",
    #         "2RLA629",
    #         "2RLA629",
    #         "3ATW723",
    #         "3CIO720",
    #         "3CIO720",
    #         "4JZY524",
    #         "4PGC938",
    #     ]
    #
    #     retrieved = sort_msd.sort_by_msd(data)
    #     expected = None
    #     self.assertEqual(retrieved, expected)


if __name__ == '__main__':
    unittest.main()
