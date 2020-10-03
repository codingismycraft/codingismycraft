class Solution(object):

    def minInteger(self, num, k):
        """Returns the minimum num based on the passed in number of flips.

        :param str num: The number to use in a string format.
        :param int k: The maximum number of flips.

        :returns: The minimum num based on the passed in number of flips.
        :type: str.
        """
        num = [int(v) for v in num]
        return ''.join([str(v) for v in self._find_min_integer(num, k)])

    def _find_min_integer(self, num, k):
        """Returns the minimum num based on the passed in number of flips.

        :param list num: The list of digits to use.
        :param int k: The maximum number of flips.

        :returns: The digits of the minimum num based on the passed in num.
        :type: list.
        """
        if not num or k <= 0:
            return num
        mix_value = None
        min_value_position = -1
        for index, value in enumerate(num):
            if index > k:
                break
            if mix_value is None or value < mix_value:
                min_value_position = index
                mix_value = value
        assert min_value_position >= 0
        remaining_flips = k - min_value_position
        value = num[min_value_position]
        del num[min_value_position]
        return [value] + self._find_min_integer(num, remaining_flips)
