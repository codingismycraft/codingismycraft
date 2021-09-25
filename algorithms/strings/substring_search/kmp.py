"""Implements the Knuth - Morris - Pratt algorithm."""


def brutal_search(string, pattern):
    """Search for pattern using a brutal approach.

    :param str string: The string to search.
    :param str pattern: The pattern to search for.

    :returns: The first matching index or None.
    :rtype: int | None.
    """
    if not string or not pattern:
        return None
    if len(pattern) <= len(string):
        for i in range(len(string) - len(pattern) + 1):
            for j in range(0, len(pattern)):
                if string[i + j] != pattern[j]:
                    break
                elif j == len(pattern) - 1:
                    return i
    return None


def kmp_search(string, pattern):
    """Search for pattern using the KMP algorithm.

    :param str string: The string to search.
    :param str pattern: The pattern to search for.

    :returns: The first matching index or None.
    :rtype: int | None.
    """
    if not string or not pattern:
        return None
    lps = make_make_lps_table(pattern)
    lps = [0] + lps
    j = 0
    i = 0

    while i < len(string):
        if string[i] == pattern[j]:
            if j + 1 == len(pattern):
                return i - j
            else:
                i += 1
                j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j]

    return None


def make_make_lps_table(pattern):
    """Creates the longest_prefix_suffix_table table for pattern.

    :param str pattern: The pattern to use.

    :returns: The LPS table as a list of integers.
    :rtype: list[int]
    """
    lps = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        if pattern[i] == pattern[j]:
            lps[i] = j + 1
            j += 1
        else:
            j = 0
    return lps
