"""Tests the lcs module."""

import unittest
import lcs

class TestLcs(unittest.TestCase):
    """Tests the lcs function."""

    def test_lcs(self):
        """Tests the lcs function."""
        s1="afd"
        s2="ads"
        expected=2
        retrieved=lcs.lcs(s1,s2)

        self.assertEqual(expected,retrieved)


    def test_empty_str(self):
        """Tests the lcs function."""
        s1=""
        s2=""
        expected=0
        retrieved=lcs.lcs(s1,s2)

        self.assertEqual(expected,retrieved)



if __name__ == '__main__':
    unittest.main()
