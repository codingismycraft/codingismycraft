"""Tests the orderly_queue module."""

import unittest

import orderly_queue


class TestOrderlyQueue(unittest.TestCase):
    """Test the solve it function."""

    def test_solve_it(self):
        """Test the solve it function."""
        solution = orderly_queue.Solution()
        retieved = solution.orderlyQueue("badckm", 3)

        print(retieved)

        retieved = solution.orderlyQueue("cba", 1)
        self.assertEqual(retieved, "acb")

        retieved = solution.orderlyQueue("baaca", 3)
        self.assertEqual(retieved, "aaabc")

        retieved = solution.orderlyQueue("xmvzi", 2)

        bad = "imvzx"
        self.assertEqual("imvxz", retieved)


if __name__ == '__main__':
    unittest.main()
