"""Implements solutions to the longest common subsequence."""


def lcs(a, b):
    """Returns the actual LCS subsequence.

    :param str a: The first string to use.
    :param str b: The second string to use.

    :return: The LCS subsequence as a string.
    :rtype: str
    """
    if not a or not b:
        return ''
    elif a[0] == b[0]:
        return a[0] + lcs(a[1:], b[1:])
    else:
        v1 = lcs(a, b[1:])
        v2 = lcs(a[1:], b)

        return v1 if len(v1) > len(v2) else v2


def count_lcs(a, b):
    """Returns the length of the longest common subsequence.

    :param str a: The first string to use.
    :param str b: The second string to use.

    :return: The length of the longest common subsequence.
    :rtype: int
    """
    if not a or not b:
        return 0
    elif a[0] == b[0]:
        return 1 + count_lcs(a[1:], b[1:])
    else:
        return max(count_lcs(a, b[1:]), count_lcs(a[1:], b))


def lcs_dynamic(s1, s2):
    """Solves the longest common subsequence using dynamic programming.

    :param str s1: The first string to use.
    :param str s2: The second string to use.

    :return: The length of the longest common subsequence.
    :rtype: int
    """
    if not s1 or not s2:
        return ''

    num_cols = len(s1) + 1
    num_rows = len(s2) + 1

    table = []
    for _ in range(0, num_rows):
        table.append([0] * num_cols)

    for row_index in range(1, num_rows):
        current_c2 = s2[row_index - 1]
        for col_index in range(1, num_cols):
            current_c1 = s1[col_index - 1]
            if current_c1 == current_c2:
                v = 1 + table[row_index - 1][col_index - 1]
            else:
                v = max(
                    table[row_index - 1][col_index],
                    table[row_index][col_index - 1]
                )
            table[row_index][col_index] = v

    return table[-1][-1]
