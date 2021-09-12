"""Sorts a list of strings by Most Significant Digit."""

ALPHABET_SIZE = 27


def get_chr_ord(c):
    y = ord(c) - ord('a') + 1
    return y


def msd_sort(strings, position, low_index, high_index):
    if high_index <= low_index or high_index - low_index == 1:
        return

    freqs = [0] * ALPHABET_SIZE

    for i in range(low_index, high_index):
        freqs[get_chr_ord(strings[i][position])] += 1

    starting_index = [low_index] * ALPHABET_SIZE
    for i in range(1, len(starting_index)):
        starting_index[i] = starting_index[i - 1] + freqs[i - 1]

    aux = [None] * len(strings)

    for i in range(low_index, high_index):
        s = strings[i]
        c = get_chr_ord(s[position])
        index_to_place_s = starting_index[c]
        aux[index_to_place_s] = s
        starting_index[c] += 1

    for i in range(low_index, high_index):
        strings[i] = aux[i]

    for i in range(len(starting_index) - 1):
        from_index = starting_index[i]
        to_index = starting_index[i + 1]
        msd_sort(strings, position+1, low_index=from_index, high_index=to_index)
