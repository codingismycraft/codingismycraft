import math
import unittest


def subsectors(s1):
    if not s1:
        return []
    head = s1[0]
    sectors = [head]
    for s in subsectors(s1[1:]):
        sectors.append(head + s)
    sectors.extend(subsectors(s1[1:]))
    return sectors


class SubsectorsTest(unittest.TestCase):
    def test_subsectors(self):
        for s in ['ab', 'abc', 'abcd']:
            expected_count = math.pow(2, len(s)) - 1
            self.assertEqual(expected_count, len(subsectors(s)))


if __name__ == '__main__':
    unittest.main()
