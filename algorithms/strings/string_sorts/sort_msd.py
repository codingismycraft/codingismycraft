"""Sorts a list of strings by Most Significant Digit."""

ALPHABET_SIZE = 256


def _get_chr_ord(string, position):
    """Returns the char index for the postion passed.

    :param str string: The string to look up.
    :param int position: The char index to use.

    :return: The index of the char in the passed in postion.
    :rtype: int
    """
    if position >= len(string):
        return 1
    c = string[position]
    y = ord(c) - 10 + 2
    return y


def msd_sort(strings, position=0, low_index=None, high_index=None):
    """Sorts in ascending order and in place the passed in array of strings.

    :param list strings: The list of the strings to sort.
    :param int position: The char position to sort by.
    :param int low_index: The low index to apply the sorting for.
    :param int high_index: The high index to apply the sorting for.
    """
    if low_index is None:
        low_index = 0
    if high_index is None:
        high_index = len(strings)

    if high_index <= low_index or high_index - low_index == 1:
        return

    freqs = [0] * ALPHABET_SIZE

    for i in range(low_index, high_index):
        freqs[_get_chr_ord(strings[i], position)] += 1

    starting_index = [low_index] * ALPHABET_SIZE
    for i in range(1, len(starting_index)):
        starting_index[i] = starting_index[i - 1] + freqs[i - 1]

    aux = [None] * len(strings)

    for i in range(low_index, high_index):
        s = strings[i]
        c = _get_chr_ord(s, position)
        index_to_place_s = starting_index[c]
        aux[index_to_place_s] = s
        starting_index[c] += 1

    for i in range(low_index, high_index):
        strings[i] = aux[i]

    for i in range(len(starting_index) - 1):
        from_index = starting_index[i]
        to_index = starting_index[i + 1]
        msd_sort(strings, position + 1, low_index=from_index,
                 high_index=to_index)
