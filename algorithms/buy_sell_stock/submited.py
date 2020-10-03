"""Expresses the solution as a class."""

class Solution(object):

    def _left_side_max_deltas(self, prices):
        """Returns a list whose each element has the max delta from left side.

        :param list prices: The list of prices.

        :return: The list with the max delta from left.
        :rtype: list.
        """
        deltas = [0] * len(prices)
        largest_so_far = None
        lower_so_far = None
        m = 0
        for index, value in enumerate(prices):
            if largest_so_far is None or largest_so_far < value:
                largest_so_far = value

            if lower_so_far is None or lower_so_far > value:
                lower_so_far = value
                largest_so_far = 0

            m = max(m, largest_so_far - lower_so_far)
            deltas[index] = m

        return deltas

    def _right_side_max_deltas(self, prices):
        """Returns a list whose each element has the max delta from right side.

        :param list prices: The list of prices.

        :return: The list with the max delta from right.
        :rtype: list.
        """
        deltas = [0] * len(prices)
        index = len(prices) - 1

        largest_so_far = None
        lower_so_far = None
        m = 0

        while index >= 0:
            value = prices[index]

            if largest_so_far is None or largest_so_far < value:
                largest_so_far = value
                lower_so_far = value

            if lower_so_far is None or lower_so_far > value:
                lower_so_far = value

            m = max(m, largest_so_far - lower_so_far)
            deltas[index] = m

            index -= 1

        return deltas

    def maxProfit(self, prices):
        m = 0
        index = 0
        left = self._left_side_max_deltas(prices)
        right = self._right_side_max_deltas(prices)
        while index < len(prices):
            m = max(m, left[index] + right[index])
            index += 1
        return m
