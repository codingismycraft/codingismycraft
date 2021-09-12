"""Sorts a list of strings by Most Significant Digit."""

ALPHABET_SIZE = 256


def get_chr_ord(c):
    y = ord(c) - ord('a') + 1
    return y


def msd_sort(strings, position, lo, hi):
    freqs = [0] * (ALPHABET_SIZE + 1)

    for i in range(lo, hi):
        freqs[get_chr_ord(strings[i][position]) + 1] += 1

    for i in range(1, len(freqs) - 1):
        freqs[i + 1] += freqs[i]

    aux = [None] * len(strings)

    for i in range(lo, hi):
        s = strings[i]
        c = get_chr_ord(s[position])
        aux[freqs[c]] = s
        freqs[c] += 1

    for i in range(lo, hi):
        strings[i] = aux[i]
    print(strings)
