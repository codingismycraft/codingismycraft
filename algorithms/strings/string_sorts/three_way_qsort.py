"""Implements a three way sort for a list of strings."""


def three_way_sort(strings, lo=None, hi=None, char_pos=None):
    """Sorts a portion the passed in strings list in place.

    :param int lo: The 0 based index of the starting index.
    :param int hi: The ending index of the portion to sort.
    :param int char_pos: The The index of the character to use for sorting.
    """
    if lo is None:
        lo = 0

    if hi is None:
        hi = len(strings) - 1

    if char_pos is None:
        char_pos = 0

    if hi - lo < 1:
        return

    head = lo
    tail = hi

    index = lo + 1

    assert 0 <= lo < hi < len(strings)

    char_to_sort_by = get_value_for_char(strings[lo], char_pos)

    while index <= tail:
        char_to_check = get_value_for_char(strings[index], char_pos)
        if char_to_check < char_to_sort_by:
            swap(strings, index, head)
            head += 1
            index += 1
        elif char_to_check > char_to_sort_by:
            swap(strings, index, tail)
            tail -= 1
        else:
            index += 1

    three_way_sort(strings, lo=lo, hi=head - 1, char_pos=char_pos)
    if char_to_sort_by > 0:
        three_way_sort(strings, lo=head, hi=tail, char_pos=char_pos + 1)
    three_way_sort(strings, lo=tail + 1, hi=hi, char_pos=char_pos)


def get_value_for_char(s, char_pos):
    """Gets the numerical value for the char in the passed in position.

    :param str s: The string to get the numerical value for.
    :param int char_pos: The postion to check.

    :return: The numerical value for the passed in position.
    """
    return ord(s[char_pos]) if char_pos < len(s) else -1


def swap(strings, index1, index2):
    """Swaps the list elements for the passed in indexes.

    :param list strings: The list of strings to use.
    :param int index1: The first index to use.
    :param int index2: The second index to use.
    """
    strings[index1], strings[index2] = strings[index2], strings[index1]
