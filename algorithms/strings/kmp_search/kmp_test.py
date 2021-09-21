"""Tests the kmp module."""

import unittest

import kmp

_TESTING_DATA = [
    [("a", "a"), 0],
    [("abcd", "a"), 0],
    [("abcd", "g"), None],
    [("abcd", "bcd"), 1],
    [("abcd", "b"), 1],
    [("abcd", "cd"), 2],
    [("abcdeabcdeabcdf", "abcdf"), 10],
]


class TestKMP(unittest.TestCase):
    """Tests the KMP solution."""

    def test_make_lps_table(self):
        """Tests the creation of the longest prefix suffix table."""
        pattern = "abcdabeabf"
        expected = [0, 0, 0, 0, 1, 2, 0, 1, 2, 0]
        retrieved = kmp.make_make_lps_table(pattern)
        self.assertListEqual(expected, retrieved)

        pattern = "aabcadaabe"
        expected = [0, 1, 0, 0, 1, 0, 1, 2, 3, 0]
        retrieved = kmp.make_make_lps_table(pattern)
        self.assertListEqual(expected, retrieved)

    def test_brutal_solution(self):
        """Tests the brutal solution."""
        for (s, p), expected in _TESTING_DATA:
            self.assertEqual(expected, kmp.brutal_search(s, p))

    def test_kmp(self):
        """Tests the KMP solution."""
        for (s, p), expected in _TESTING_DATA:
            self.assertEqual(expected, kmp.kmp_search(s, p))


if __name__ == '__main__':
    unittest.main()
