"""Implements quick sort to compare it with key indexed sorting."""


def qsort(data, low=None, high=None, less_than=None):
    """Sorts in-place the passed in data."""
    if low is None:
        low = 0
    if high is None:
        high = len(data) - 1
    if high <= low:
        return
    if not less_than:
        less_than = lambda obj1, obj2: obj1 < obj2
    pivot = _partition(data, low, high, less_than)
    qsort(data, low, pivot - 1, less_than)
    qsort(data, pivot + 1, high, less_than)


def _partition(data, start, end, less_than):
    """Partitions the passed in data."""
    assert start < end
    low = start
    index = start
    while index <= end - 1:
        if less_than(data[index], data[end]):
            _swap(data, index, low)
            low += 1
        index += 1
    if not less_than(data[low], data[end]):
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
    print(a)
    a = [
        ("jas", 10), ("adsf", 1), ("asdsa", 9),
        ("a", 4), ("asa", 3), ("af", 4), ("zz", 1)
    ]
    qsort(a, less_than=lambda obj1, obj2: obj1[1] < obj2[1])
    print(a)
