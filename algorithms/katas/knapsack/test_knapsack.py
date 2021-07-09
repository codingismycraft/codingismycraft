import unittest

import knapsack

TESTING_DATA = [
    {
        'items': [
            knapsack.Item(w=1, v=1),
            knapsack.Item(w=3, v=4),
            knapsack.Item(w=4, v=5),
            knapsack.Item(w=5, v=7),
            knapsack.Item(w=2, v=4),
        ],
        'capacity': 9,
        'expected_value': 13
    },
    {
        'items': [
            knapsack.Item(w=8, v=17),
            knapsack.Item(w=4, v=12),
            knapsack.Item(w=3, v=6),
        ],
        'capacity': 10,
        'expected_value': 18
    }

]




class TestKnapsack(unittest.TestCase):

    def test1(self):
        weights = [8, 4, 3, 5, 1]
        values = [17, 12, 6, 12, 2]
        max_capacity = 10
        expected_value = 26
        self.assertEqual(
            expected_value,
            knapsack.solve_bags(weights, values, max_capacity)
        )

    def test2(self):
        weights = [8, 4, 3]
        values = [17, 12, 6]
        max_capacity = 10
        expected_value = 18
        self.assertEqual(
            expected_value,
            knapsack.solve_bags(weights, values, max_capacity)
        )

    def test3(self):
        weights = [1, 3, 4, 5, 2]
        values = [1, 4, 5, 7, 4]
        max_capacity = 9
        expected_value = 13
        self.assertEqual(
            expected_value,
            knapsack.solve_bags(weights, values, max_capacity)
        )

    def test4(self):
        weights = [8, 4, 3, 5, 1]
        values = [17, 12, 6, 12, 2]
        max_capacity = 10
        expected_value = 26
        self.assertEqual(
            expected_value,
            knapsack.solve_bags(weights, values, max_capacity)
        )



if __name__ == '__main__':
    unittest.main()
