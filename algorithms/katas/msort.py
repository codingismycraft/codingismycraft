import unittest


def merge(a1, a2):
    i1, i2 = 0, 0
    merged = []
    while i1 < len(a1) and i2 < len(a2):
        if a1[i1] < a2[i2]:
            merged.append(a1[i1])
            i1 += 1
        else:
            merged.append(a2[i2])
            i2 += 1

    while i1 < len(a1):
        merged.append(a1[i1])
        i1 += 1

    while i2 < len(a2):
        merged.append(a2[i2])
        i2 += 1

    return merged


def msort(a, start, end):
    if start == end:
        return [a[start]]
    assert start < end
    middle = start + (end - start) // 2
    a1 = msort(a, start, middle)
    a2 = msort(a, middle + 1, end)
    return merge(a1, a2)


class MSortTest(unittest.TestCase):
    def test_msort(self):
        a = [1, 9, 7, 2, 12, 21, 0]
        b = msort(a, 0, len(a) - 1)
        self.assertListEqual(sorted(a), b)


if __name__ == '__main__':
    unittest.main()

