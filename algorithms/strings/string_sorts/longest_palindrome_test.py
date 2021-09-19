"""Tests the longest_palindrome module."""

import unittest

import longest_palindrome as lp


class TestLongestPalindrome(unittest.TestCase):
    """Tests the PalindromeSolver class."""

    _TESTING_DATA = [
        ("zaaf", "aa"),
        ("aaaf", "aaa"),
        ("aaaa", "aaaa"),
        ("babad", "bab"),
        ("cbbd", "bb"),
        ("a", "a"),
        ("ac", "a"),
        ("aacabdkacaa", "aca")
    ]

    def test_dynamic_programming_solution(self):
        """Test the DP longest palindrome method."""

        solution = lp.DPSolution()

        for s, expected in self._TESTING_DATA:
            self.assertEqual(solution.longestPalindrome(s), expected)

    def test_solution(self):
        """Test the longest palindrome solution."""

        solution = lp.Solution()

        for s, expected in self._TESTING_DATA:
            self.assertEqual(solution.longestPalindrome(s), expected)


if __name__ == '__main__':
    unittest.main()
