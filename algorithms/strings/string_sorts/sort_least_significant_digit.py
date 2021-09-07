"""Implements the least significant digit sort."""


def lsd_sort(data):
    data = [d.strip() for d in data]
    length = len(data[0])
    _verify_lengths(data, length)
    sorted_data = [None] * len(data)
    for digit_index in range(length, 0, -1):
        digit_index -= 1
        _key_sort(data, sorted_data, digit_index)
        data, sorted_data = sorted_data, data
    return data


def _key_sort(data, sorted_data, digit_index):
    assert len(data) == len(sorted_data)
    frequencies = [0] * 256
    for string in data:
        frequencies[ord(string[digit_index])] += 1

    accumulated_frequencies = [0] * 256
    for i in range(1, 256):
        accumulated_frequencies[i] = accumulated_frequencies[i - 1] + \
                                     frequencies[i]

    starting_indexes = [0] * 256
    for i in range(1, 256):
        starting_indexes[i] = accumulated_frequencies[i - 1]

    for string in data:
        digit = ord(string[digit_index])
        index = starting_indexes[digit]
        sorted_data[index] = string
        starting_indexes[digit] += 1

    return sorted_data


def _verify_lengths(data, length):
    for d in data:
        assert len(d) == length
