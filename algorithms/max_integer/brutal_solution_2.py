"""Implements a brutal soltution for the min integer algorithm."""


def minInteger(num, k):
    """Returns the minimum num based on the passed in number of flips.

    :param str num: The number to use in a string format.
    :param int k: The maximum number of flips.

    :returns: The minimum num based on the passed in number of flips.
    :type: str.
    """
    num = [int(v) for v in num]
    indexes = make_matching_indexes(num)
    prefix = []
    while k > 0:
        element, m = get_next_element(indexes, k)
        if m is None:
            break
        prefix.append(element)
        decrease_elements(indexes, m)
        k -= m
    suffix = get_remaining_indexes(indexes)
    values = prefix + suffix
    return ''.join(str(x) for x in values)


def decrease_elements(indexes, k, count=1):
    for i in range(0, 10):
        for j, v in enumerate(indexes[i]):
            if v >= k:
                indexes[i][j] -= count


def get_remaining_indexes(indexes):
    remaining_indexes = []
    for i in range(0, 10):
        for j, v in enumerate(indexes[i]):
            remaining_indexes.append((v, i))
    remaining_indexes.sort(key=lambda x: x[0])
    return [x for _, x in remaining_indexes]


def get_next_element(indexes, k):
    for i in range(0, 10):
        values = indexes[i]
        for j in range(0, len(values)):
            if values[j] <= k:
                v = values[j]
                del values[j]
                return i, v
    return None, None


def make_matching_indexes(values):
    matches = [[] for _ in range(0, 10)]
    for index, v in enumerate(values):
        matches[v].append(index)
    return matches
