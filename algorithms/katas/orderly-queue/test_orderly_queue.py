"""Tests the orderly_queue module."""

import unittest

import orderly_queue


class TestOrderlyQueue(unittest.TestCase):
    """Test the solve it function."""

    def test_solve_it(self):
        """Test the solve it function."""
        # retieved = orderly_queue.solve_it("badckm", 3)
        #
        # print(retieved)
        #
        # retieved = orderly_queue.solve_it("cba", 1)
        # self.assertEqual(retieved, "acb")
        #
        # retieved = orderly_queue.solve_it("baaca", 3)
        # self.assertEqual(retieved, "aaabc")

        retieved = orderly_queue.solve_it("xmvzi", 2)

        bad = "imvzx"
        self.assertEqual("imvxz", retieved)







if __name__ == '__main__':
    unittest.main()


