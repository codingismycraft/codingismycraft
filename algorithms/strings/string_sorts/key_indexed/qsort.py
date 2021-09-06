"""Implements quick sort to compare it with key indexed sorting."""


def qsort(data, low=None, high=None):
    """Sorts in-place the passed in data."""
    if low is None:
        low = 0
    if high is None:
        high = len(data) - 1
    if high <= low:
        return
    pivot = _partition(data, low, high)
    qsort(data, low, pivot - 1)
    qsort(data, pivot + 1, high)


def _partition(data, start, end):
    """Partitions the passed in data."""
    assert start < end
    low = start
    index = start
    while index <= end - 1:
        if data[index] < data[end]:
            _swap(data, index, low)
            low += 1
        index += 1
    if data[low] > data[end]:
        _swap(data, low, end)
    return low


def _swap(data, i1, i2):
    """Swaps the passint in positions.."""
    data[i1], data[i2] = data[i2], data[i1]


if __name__ == '__main__':
    # Self-test.
    a = [10, 9, 4, 3, 4, 1]
    qsort(a)
    assert a == sorted(a)
