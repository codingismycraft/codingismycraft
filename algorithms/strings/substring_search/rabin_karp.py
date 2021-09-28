"""Implements rabin-karp string matching algorithm."""

_SEED = 997


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
    p_length = len(pattern)
    for k, c in enumerate(pattern):
        pattern_hash += (ord(c) * _SEED ** (p_length - k - 1)) % _SEED
        rolling_hash += (ord(text[k]) * _SEED ** (p_length - k - 1)) % _SEED

    pattern_hash = pattern_hash % _SEED
    rolling_hash = rolling_hash % _SEED
    for i in range(len(text) - p_length + 1):
        if i > 0:
            rolling_hash -= (ord(text[i - 1]) * _SEED ** (p_length - 1)) % _SEED
            rolling_hash *= _SEED
            rolling_hash += ord(text[i + p_length - 1])
            rolling_hash = rolling_hash % _SEED
        if pattern_hash == rolling_hash:
            if pattern == text[i: i + p_length]:
                return i
    return None
