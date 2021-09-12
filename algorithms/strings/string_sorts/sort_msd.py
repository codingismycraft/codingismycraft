"""Sorts a list of strings by Most Significant Digit."""

ALPHABET_SIZE = 256


def get_chr_ord(c):
    y = ord(c) - ord('a') + 1
    return y


def msd_sort(strings, position, lo, hi):
    freqs = [0] * (ALPHABET_SIZE + 1)

    for i in range(lo, hi):
        freqs[get_chr_ord(strings[i][position])+1] += 1

    for i in range(1, len(freqs)-1):
        freqs[i + 1] += freqs[i]

    aux = [None] * len(strings)
    for i, s in enumerate(strings):
        c = get_chr_ord(s[position])
        aux[freqs[c]] = s
        freqs[c] += 1
    print(aux)





def msd_sort1(strings, position, lo, hi):
    """Sorts strings in the range lo-hi based on the char in passed position.

    :param list strings: A list of strings.
    :param int position: The char position to sort by.
    :param int lo: The lower index to sort from.
    :param int hi: The upper index to sort to.
    """

    if position >= 3:
        return
    if lo == hi or hi < 0 or hi < lo:
        return
    if hi < lo:
        return
    assert lo >= 0, "Lo must be larger than 0."
    assert lo < hi, "Lo must be less than hi."
    assert hi < len(strings), "Hi must be less than len(strings)."

    # Count Frequencies
    frequencies = [0] * ALPHABET_SIZE
    for i in range(lo, hi + 1):
        s = strings[i]
        p = get_chr_ord(s[position])
        frequencies[p+1] += 1


def _show_frequencies(frequencies):
    """Used for debugging only."""
    for i, f in enumerate(frequencies):
        if f > 0:
            print(chr(i), f)
