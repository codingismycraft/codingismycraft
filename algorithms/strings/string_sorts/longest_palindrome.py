"""Implements a dynamic programming solution to longest palindrome."""


class DPSolution:
    """Dynamic programming solution to longest palindrome

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
