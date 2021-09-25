"""Exposes the bm_search function."""

# Aliases.
_ALPHABET_SIZE = 256


def bm_search(text, substring):
    """Search for the passed in substring in the text.

    :param str text: The text to search.
    :param str substring: The substring to search for.

    :returns: The matching index or None if no match.
    :rtype: int or None.
    """
    if not text or not substring or len(substring) > len(text):
        return None
    right = [-1] * _ALPHABET_SIZE
    for pos, c in enumerate(substring):
        right[ord(c)] = pos
    i = 0
    while i <= len(text) - len(substring):
        skip = 0
        for j in range(len(substring) - 1, -1, -1):
            if text[i+j] != substring[j]:
                x = j - right[ord(text[i+j])]
                skip = x if x >= 0 else 1
                break
        if skip == 0:
            return i
        i += skip
    return None



