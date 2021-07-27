"""Tests the lcs_recursive module."""

import unittest

import lcs


class TestRecursive(unittest.TestCase):
    """Tests the solutions to lcs."""

    def test_solutions(self):
        """Tests the solutions to lcs."""
        s1 = "ABAZDC"
        s2 = "BACBAD"
        expected = "ABAD"

        retrieved = lcs.count_lcs(s1, s2)
        self.assertEqual(retrieved, len(expected))

        retrieved = lcs.lcs(s1, s2)
        self.assertEqual(retrieved, expected)


if __name__ == '__main__':
    unittest.main()
