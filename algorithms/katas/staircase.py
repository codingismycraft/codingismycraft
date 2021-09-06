"""Solves the climbing stairs problem in O(1) with one line.

See also: https://leetcode.com/problems/climbing-stairs/
"""

import math

A = math.sqrt(5)
B = 1 / A


def climbStairs(n):
    return int(
        B * (((1 + A) / 2) ** (n + 1)) - B * (((1 - A) / 2) ** (n + 1)) + 0.1)


class Solution:
    def climbStairs(self, n):
        return int(B * (((1 + A) / 2) ** (n + 1)) - B * (
                    ((1 - A) / 2) ** (n + 1)) + 0.1)


if __name__ == '__main__':
    solution = Solution()
    assert solution.climbStairs(2) == 2
    assert solution.climbStairs(3) == 3
    assert solution.climbStairs(45) == 1836311903
