import unittest

import three_sum


class ThreeSumTest(unittest.TestCase):
    def test_three_sum(self):
        """Changed after cloning..."""
        values = [-1, 0, 1, 2, -1, -4]

        expected = [[-1, -1, 2], [-1, 0, 1]]

        retrieved = three_sum.three_sum(values)
        print(retrieved)

    # def test_three_sum2(self):
    #     values = [-1, 0, 1]
    #
    #     retrieved = three_sum.three_sum(values)
    #     print(retrieved)


if __name__ == '__main__':
    unittest.main()
