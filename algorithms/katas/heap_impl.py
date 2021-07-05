"""Exposes the implementation of heap."""


def push(heap, value):
    """Pushes a new value to the heap.

    :param list heap: The heap to push the value.
    :param value: The value to push.
    """
    heap.append(value)
    _move_upwards(heap, len(heap) - 1)


def pop(heap):
    """Pops the first value of the heap.

    :param list heap: The heap from which the value will be popped.
    """
    if not heap:
        return None
    v = heap.pop(0)
    if not heap:
        return v
    last_value = heap.pop()
    heap.insert(0, last_value)
    _move_downwards(heap, 0)
    return v


def _get_parent(index):
    if index <= 0:
        return -1
    if index % 2 == 0:
        index -= 1
    return index // 2


def _get_children(index):
    if index < 0:
        return -1
    left = index * 2 + 1
    right = left + 1
    return left, right


def _move_upwards(heap, index):
    if index < 0:
        return
    parent_index = _get_parent(index)
    if parent_index < 0:
        return
    if heap[parent_index] > heap[index]:
        _swap(heap, parent_index, index)
        _move_upwards(heap, parent_index)


def _swap(heap, index1, index2):
    heap[index1], heap[index2] = heap[index2], heap[index1]


def _move_downwards(heap, index):
    left, right = _get_children(index)
    if left >= len(heap):
        return
    if right >= len(heap):
        right = left
    if heap[left] < heap[right]:
        lowest = left
    else:
        lowest = right
    if heap[index] > heap[lowest]:
        _swap(heap, index, lowest)
        _move_downwards(heap, index)
