"""Implements quicksort."""


def partition(data, i1, i2):
    """Places a pivot element in its sorted index.

    :param list data: The list to sort.
    :param int i1: The starting index of the piece to sort.
    :param int i2: The ending index of the piece to sort.

    :returns: The index of the sorted item.
    :rtype: int.
    """
    assert i2 >= i1

    if i2 == i1:
        return i1

    pivot_index = (i2 - i1) // 2 + i1
    data[pivot_index], data[i2] = data[i2], data[pivot_index]

    lo = i1
    high = i2 - 1

    while True:
        while lo < i2 and data[lo] <= data[i2]:
            lo += 1
        while high >= i1 and data[high] >= data[i2]:
            high -= 1
        if lo <= high:
            data[lo], data[high] = data[high], data[lo]
        else:
            break

    data[i2], data[lo] = data[lo], data[i2]
    return lo


def qsort(data, i1=0, i2=None):
    """Sorts the section of data between i1 - i2.

    :param list data: The list to sort.
    :param int i1: The starting index of the piece to sort.
    :param int i2: The ending index of the piece to sort.
    """
    if i2 is None:
        i2 = len(data) - 1
    if 0 <= i1 < i2:
        i = partition(data, i1, i2)
        qsort(data, i1, i - 1)
        qsort(data, i + 1, i2)
