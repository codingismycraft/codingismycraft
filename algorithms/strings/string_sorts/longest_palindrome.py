"""Implements a dynamic programming solution to longest palindrome."""


class DPSolution:
    """Dynamic programming solution to longest palindrome.

    :cvar list[list[int]] _matrix: Memoizes the is palindrome table.
    """
    _matrix = [[0] * 1000 for _ in range(1000)]

    def longestPalindrome(self, s):
        """Find the longest palindrome substring in the passed string s.

        :param str s: The string to use.

        :returns: The longest palindrome substring.
        :rtype: str
        """
        max_palindrome = s[0]
        for start_col in range(len(s)):
            row = 0
            for col in range(start_col, len(s)):
                if start_col == 0:
                    self._matrix[row][col] = 1
                elif start_col == 1:
                    self._matrix[row][col] = 1 if s[col] == s[row] else 0
                elif s[col] != s[row]:
                    self._matrix[row][col] = 0
                else:
                    self._matrix[row][col] = self._matrix[row + 1][col - 1]
                if self._matrix[row][col] == 1 and col - row > len(
                        max_palindrome) - 1:
                    max_palindrome = s[row:col + 1]
                row += 1
        return max_palindrome


class Solution:
    """Solution to longest palindrome."""

    @classmethod
    def check(cls, s, left, right):
        """Checks if the passed in left and right are palindrome borders.

        :param str s: The string to check for palindrome.
        :param int left: The left index to check.
        :param int right: The right index to check.

        :returns: True if the passed in left and right are palindrome borders.
        :rtype: int.
        """
        return left >= 0 and right < len(s) and s[left] == s[right]

    def longestPalindrome(self, s):
        """Find the longest palindrome substring in the passed string s.

        :param str s: The string to use.

        :returns: The longest palindrome substring.
        :rtype: str
        """
        picked_left = 0
        picked_right = 0

        for position in range(0, len(s)):
            left = position
            right = position
            while self.check(s, left - 1, right + 1):
                left -= 1
                right += 1
            if picked_right - picked_left < right - left:
                picked_left = left
                picked_right = right

            left = position
            right = position + 1
            if self.check(s, left, right):
                while self.check(s, left - 1, right + 1):
                    left -= 1
                    right += 1
                if picked_right - picked_left < right - left:
                    picked_left = left
                    picked_right = right

        return s[picked_left:picked_right + 1]
