"""Tests the boyer_moore module."""

import unittest

import boyer_moore

# Aliases.
bm_search = boyer_moore.bm_search

class TestBoyerMoore(unittest.TestCase):
    """Tests the boyer_moore module."""

    _TESTING_DATA = [
        [("a", "a"), 0],
        [("abcd", "a"), 0],
        [("ab", "g"), None],
        [("abcd", "g"), None],
        [("abcd", "bc"), 1],
        [("abcd", "bc"), 1],
        [("abcd", "bcd"), 1],
        [("abcd", "b"), 1],
        [("abcd", "cd"), 2],
        [("abcdeabcdeabcdf", "abcdf"), 10],
        [("abababababababxbab", "ababx"), 10],
        [("abababababx", "babx"), 7],
        [("abababx", "babx"), 3],
    ]

    def test_bm_search(self):
        """Tests the bm_search function."""
        for (s, p), expected in self._TESTING_DATA:
            retrieved = bm_search(s, p)
            self.assertEqual(expected, retrieved)


if __name__ == '__main__':
    unittest.main()
