"""Counts the number of possible decoded strings."""

import functools


@functools.lru_cache()
def count_matches(data):
    """Counts the number of possible decoded strings.

    :param str data: A string consisting of digits.

    :return: The number of possible decoded strings.
    """
    if not data:
        return 1
    elif data[0] == '0':
        return 0
    elif len(data) == 1:
        return 1
    elif int(data[0:2]) <= 26:
        return count_matches(data[1:]) + count_matches(data[2:])
    else:
        return count_matches(data[1:])
