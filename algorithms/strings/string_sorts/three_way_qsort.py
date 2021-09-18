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

    char_to_sort_by = ord(strings[lo][char_pos]) if char_pos < len(strings[lo]) else -1

    while index <= tail:
        #char_to_check =
        if _less_than(strings[index], c,  char_pos):
            swap(strings, index, head)
            head += 1
            index += 1
        elif _more_than(strings[index], c,  char_pos):
            swap(strings, index, tail)
            tail -= 1
        else:
            index += 1

    three_way_sort(strings, lo=lo, hi=head-1, char_pos=char_pos)
    three_way_sort(strings, lo=head, hi=tail, char_pos=char_pos + 1)
    three_way_sort(strings, lo=tail+1, hi=hi, char_pos=char_pos)


def swap(strings, index1, index2):
    """Swaps the list elements for the passed in indexes.

    :param list strings: The list of strings to use.
    :param int index1: The first index to use.
    :param int index2: The second index to use.
    """
    strings[index1], strings[index2] = strings[index2], strings[index1]


def _less_than(s1, s2, char_pos):
    """Compares strings based on a contained character.

    :param str s1: The left hand string to compare.
    :param str s2: The right hand string to compare.
    :param int char_pos: The index of the character to use.

    :return: True if the the char to compare is smaller in s1:
    :rtype: bool
    """
    v1 = ord(s1[char_pos]) if char_pos < len(s1) else -1
    v2 = ord(s2[char_pos]) if char_pos < len(s2) else -1

    return v1 < v2


def _more_than(s1, s2, char_pos):
    """Compares strings based on a contained character.

    :param str s1: The left hand string to compare.
    :param str s2: The right hand string to compare.
    :param int char_pos: The index of the character to use.

    :return: True if the the char to compare is smaller in s2:
    :rtype: bool
    """
    v1 = ord(s1[char_pos]) if char_pos < len(s1) else -1
    v2 = ord(s2[char_pos]) if char_pos < len(s2) else -1

    return v1 > v2

