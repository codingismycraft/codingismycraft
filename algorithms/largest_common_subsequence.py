import functools

@functools.lru_cache()
def lcs(a, b):
    if not a or not b:
        return 0
    if a[-1] == b[-1]:
        return 1 + lcs(a[0:-1], b[0:-1])
    else:
        return max(lcs(a[0:-1], b), lcs(b[0:-1], a))


if __name__ == '__main__':
    a = "ABAZDC"
    b = "BACBAD"
    expected = "ABAD"
    assert len(expected) == lcs(a, b)
