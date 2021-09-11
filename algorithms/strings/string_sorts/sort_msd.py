"""Sorts a list of strings by Most Significant Digit."""

ALPHABET_SIZE = 256


def msd_sort(strings, position, lo, hi):
    """Sorts strings in the range lo-hi based on the char in passed position.

    :param list strings: A list of strings.
    :param int position: The char position to sort by.
    :param int lo: The lower index to sort from.
    :param int hi: The upper index to sort to.
    """
    assert 0 <= lo < hi < len(strings)

    # Count Frequencies
    frequencies = [0] * ALPHABET_SIZE
    for i in range(lo, hi + 1):
        s = strings[i]
        frequencies[ord(s[position])] += 1

    # Count cumulative frequencies
    cumulative_frequencies = [0] * ALPHABET_SIZE
    for i in range(1, ALPHABET_SIZE):
        cumulative_frequencies[i] = frequencies[i-1] + cumulative_frequencies[i-1]

    aux = [None] * len(strings)
    for i in range(lo, hi + 1):
        s = strings[i]
        c = ord(s[position])
        p = cumulative_frequencies[c]
        aux[p+ lo] = s
        cumulative_frequencies[c] += 1

    print(aux)
    for i in range(lo, hi + 1):
        strings[i] = aux[i]











def _show_frequencies(frequencies):
    """Used for debugging only."""
    for i, f in enumerate(frequencies):
        if f > 0:
            print(chr(i), f)
