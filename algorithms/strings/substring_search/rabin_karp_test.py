"""Tests the Rabin Karp module."""

import unittest

import rabin_karp

# Aliases.
rabin_karp_search = rabin_karp.rabin_karp_search


class TestRabinKarp(unittest.TestCase):
    """Tests the rabin-karp module."""

    _TESTING_DATA = [
        [("a", "a"), 0],
        [("abcd", "a"), 0],
        [("abcd", "g"), None],
        [("abcd", "bcd"), 1],
        [("abcd", "b"), 1],
        [("abcd", "cd"), 2],
        [("abcdeabcdeabcdf", "abcdf"), 10],
        [("abababababababxbab", "ababx"), 10],
        [("abababababx", "babx"), 7],
        [("abababx", "babx"), 3],
    ]

    def test_rabin_karp_search(self):
        """Test the rabin_karp_search function."""
        for (s, p), expected in self._TESTING_DATA:
            self.assertEqual(expected, rabin_karp_search(s, p))


if __name__ == '__main__':
    unittest.main()
