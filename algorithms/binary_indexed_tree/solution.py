"""Brutal solution of running_count."""


class BrutalRunningCount:
    """Brutal solution of running_count.

    :ivar list _running_count: Holds the running count by index.
    """

    _running_count = None

    def __init__(self, values):
        """Initializer.

        Creates a list holding the running count for every index in
        the passed in values.
        
        :param list values: List of integers. 
        """
        self._running_count = [values[0]]
        for index in range(1, len(values)):
            self._running_count.append(self._running_count[-1] + values[index])

    def get_total(self, index):
        """Returns the sum from 0 to index.

        :param int index: The index to calculate the sum for.

        :return: The sum from 0 to index.
        :rtype: int.
        """
        return self._running_count[int(index)]

    def increase(self, index, value):
        """Increases sums by value after index.

        Since the stored values are running counts, after we increase
        the value for the passed-in index we do the same until the end
        of the stored list to keep sums in sync.

        :param int index: Where to add the value.
        :param int value: The value to add.
        """
        while index < len(self._running_count):
            self._running_count[index] += value
            index += 1


class RunningCount:
    """Solution for running_count.

    :ivar list _running_count: Holds the running count by index.
    """

    _running_count = None

    def __init__(self, values):
        """Initializer.

        :param list values: List of integers.
        """
        self._running_count = [0] * (len(values) + 1)
        for index in range(1, len(self._running_count)):
            k = index
            c = index & -index
            v = 0
            count = 0
            while count < c:
                v += values[k - 1]
                k -= 1
                count += 1
            self._running_count[index] = v

    def get_total(self, index):
        """Returns the sum from 0 to index.

        Sums the running count for the passed in index and all
        the other indexes that depend on it.

        :param int index: The index to calculate the sum for.

        :return: The sum from 0 to index.
        :rtype: int.
        """
        index += 1
        total = 0
        while index:
            total += self._running_count[index]
            index = index - (index & -index)
        return total

    def increase(self, index, value):
        """Increases sums by value after index.

        Increases the running count for the affected index and all
        the other indexes that depend on it.

        :param int index: Where to add the value.
        :param int value: The value to add.
        """
        index += 1
        while index < len(self._running_count):
            self._running_count[index] += value
            index = index + (index & -index)
