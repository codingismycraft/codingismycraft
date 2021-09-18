"""Tests sorting by most significant digit."""

import unittest



import three_way_qsort



class TestThreeWaySort(unittest.TestCase):
    """Tests sorting by most significant digit."""

    def test_less_than(self):
        """Tests the less than function."""

        _less_than = three_way_qsort._less_than
        _more_than = three_way_qsort._more_than

        s1 = 'zzza'
        s2 = 'aaab'

        self.assertTrue(_less_than(s1, s2, 3))
        self.assertFalse(_less_than(s2, s1, 3))

        self.assertFalse(_more_than(s1, s2, 3))
        self.assertTrue(_more_than(s2, s1, 3))

        s1 = 'zzz'
        s2 = 'aaab'

        self.assertTrue(_less_than(s1, s2, 3))
        self.assertFalse(_less_than(s2, s1, 3))

        self.assertFalse(_more_than(s1, s2, 3))
        self.assertTrue(_more_than(s2, s1, 3))

    def test_three_way_qsort(self):
        # data = [
        #     'dda',
        #     'adb  ',
        #     'acc',
        #     'zab   ',
        #     'zxy',
        #     'zaasas',
        #     'bad',
        #     'aaaab ',
        #     'aaak',
        #     'aaaabcddd',
        #     'bae',
        #     'zxy',
        # ]

        data = [
            #'dda',
            'adb',
            'adb',
            # 'acc',
            # 'zab',
            # 'zxy',
            # 'zaasas',
            # 'bad',
            # 'aaaab ',
            # 'aaak',
            # 'aaaabcddd',
            # 'bae',
            #'zxy',
        ]


        strings = data[:]
        three_way_qsort.three_way_sort(strings)

        print("retrieved:", strings)
        expected = sorted(strings)
        print(expected)
        self.assertListEqual(expected, strings)


if __name__ == '__main__':
    unittest.main()
