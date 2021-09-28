"""Implements rabin-karp string matching algorithm."""

_SEED = 997


def _hash_for_char(c):
    return ord(c)
    return ord(c) - ord('a') + 1


def rabin_karp_search(text, pattern):
    """Searches in text for substring.

    :param str text: The text to search.
    :param str pattern: The substring to search for.

    :return: The index of the substring in text or None.
    :rtype: int or None.
    """
    if not text or not pattern or len(pattern) > len(text):
        return None

    pattern_hash = 0
    rolling_hash = 0
    for k, c in enumerate(pattern):
        pattern_hash += (_hash_for_char(c) * _SEED ** (len(pattern) - k - 1)) % _SEED
        rolling_hash += (_hash_for_char(text[k]) * _SEED ** (len(pattern) - k - 1)) % _SEED

    pattern_hash = pattern_hash % _SEED
    rolling_hash = rolling_hash % _SEED
    for i in range(len(text) - len(pattern) + 1):
        if i > 0:
            rolling_hash -= (_hash_for_char(text[i-1]) * _SEED ** (len(pattern)-1))  % _SEED
            rolling_hash *= _SEED
            rolling_hash += _hash_for_char(text[i+len(pattern)-1])
            rolling_hash = rolling_hash % _SEED
        if pattern_hash == rolling_hash:
            if pattern == text[i: i + len(pattern)]:
                return i
    return None


























