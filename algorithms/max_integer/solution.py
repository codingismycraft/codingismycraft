"""Exposes the minInteger function. 

Solves the Minimum Possible Integer After at Most K 
Adjacent Swaps On Digits.
"""


def minInteger(num, k):
    """Returns the minimum num based on the passed in number of flips.

    :param str num: The number to use in a string format.
    :param int k: The maximum number of flips.

    :returns: The minimum num based on the passed in number of flips.
    :type: str.
    """
    num = [int(v) for v in num]
    removals = _Index([0 for _ in range(len(num))])
    indexes = _make_matching_indexes(num)
    prefix = []
    try:
        while k > 0:
            element, k = _get_next_element(indexes, k, removals)
            prefix.append(element)
    except _NoMoreFlipException:
        pass
    suffix = _get_remaining_indexes(indexes)
    values = prefix + suffix
    return ''.join(str(x) for x in values)


class _NoMoreFlipException(Exception):
    """Raised when there no possible digit flip to stop iteration."""


class _Index:
    """Implements a Fenwick binary Indexed Tree.

    :ivar list _index: Holds the partial sums to use for the calculations
    of the sums.
    """

    _index = None

    def __init__(self, values):
        """Initializer.

        Builds the index.

        :param list values: List of integers.
        """
        self._index = [0]
        for i in range(0, len(values)):
            total = 0
            l = 1 + i
            k = l & -l
            for j in range(k):
                total += values[i - j]
            self._index.append(total)

    def get_sum(self, index):
        """Returns the sum from 0 to index.

        :param int index: The index to return the sum for.
        :rtype: int.
        """
        index += 1
        total = self._index[index]
        while True:
            index = index - (index & -index)
            if index <= 0:
                break
            total += self._index[index]
        return total

    def increase(self, index, value):
        """Increases the sum in a specific index by a value.

        :param int index: The index to increase the sum for.
        :param int value: The increment value.
        """
        index += 1
        while index < len(self._index):
            self._index[index] += value
            index = index + (index & -index)


def _get_next_element(indexes, k, removals):
    """Returns the next smaller digit to bring in front and the remaining flips.

    :param list indexes: A two dimensional list holding the occurrences of
    every digit in the passed in values list.

    :param k: The maximum number of flips allowed.

    :param _Index removals: A Fenwick binary Indexed Tree holding the removals
    for each position.

    :return: A tuple consisting of:
        The next smaller digit to bring in front and the remaining flips.
        The remaining number of flips.
    :rtype: tuple.

    :raises: _NoMoreFlipException: When no flip can occur.
    """
    for i in range(0, 10):
        values = indexes[i]
        if not values:
            continue
        r = removals.get_sum(values[0])
        if values[0] <= (k - r):
            y = values[0]
            del values[0]
            removals.increase(y, -1)
            return i, k - y - r
    raise _NoMoreFlipException


def _make_matching_indexes(values):
    """Returns the matching indexes based on the passed-in values.

    The matching index is a two dimensional list having 10 rows (once for
    each digit from 0..9).

    The index of each row corresponds to a digit from 0..9 while its contents
    hold all the indexes where it appears in the passed in values list.

    Example:

    Passing values = [3, 9, 0, 6, 5, 6, 9, 3, 5, 8]

    will return:
            [
                [2],
                [],
                [],
                [0, 7],
                [],
                [4, 8],
                [3, 5],
                [],
                [9],
                [1, 6]
            ]


    :param list values: A list of digits.

    :return: A two dimensional list holding the occurrences of every digit
    in the passed in values list.

    :rtype: list.
    """
    matches = [[] for _ in range(0, 10)]
    for index, v in enumerate(values):
        matches[v].append(index)
    return matches


def _get_remaining_indexes(indexes):
    """Returns the left-over digit indexes (sorted from lower to higher).

    Used to construct the unsorted part of the remaining digits that
    was not changed after there are no more remaining flips.

    Example

    Passing indexes as:
        [
            [],
            [],
            [],
            [0, 7],
            [],
            [8],
            [3, 5],
            [],
            [9],
            [6]
        ]

    will return:

    [3, 6, 6, 9, 3, 5, 8]

    :param list indexes: A two dimensional array holding the occurrences of
    each decimal digits.

    :return: The left-over digit indexes (sorted from lower to higher).
    :rtype: list.
    """
    remaining_indexes = []
    for i in range(0, 10):
        for j, v in enumerate(indexes[i]):
            remaining_indexes.append((v, i))
    remaining_indexes.sort(key=lambda x: x[0])
    return [x for _, x in remaining_indexes]


class Solution(object):
    
    def minInteger(self, num, k):
        """Returns the minimum num based on the passed in number of flips.

        :param str num: The number to use in a string format.
        :param int k: The maximum number of flips.

        :returns: The minimum num based on the passed in number of flips.
        :type: str.
        """
        return minInteger(num, k)
