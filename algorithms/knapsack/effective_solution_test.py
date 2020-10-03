"""Tests the solution to knapsack problem."""

import collections
import random
import unittest

import brutal_solution
import effective_solution

Item = collections.namedtuple("Item", ['name', 'value', 'weight'])


class SolutionTest(unittest.TestCase):
    """Tests the solution to knapsack problem."""

    def test_effective_solution(self):
        """Tests the effective solution."""
        items = [
            Item(name='guitar', value=1500, weight=1),
            Item(name='laptop', value=2000, weight=3),
            Item(name='stereo', value=3000, weight=4),
        ]
        self.assertEqual(effective_solution.solve(4, items), 3500)
        self.assertEqual(brutal_solution.solve(4, items), 3500)

    def test_shuffles_items(self):
        """Tests the effective solution reshuffling lists."""
        items = [
            Item(name='junk', value=50, weight=3),
            Item(name='guitar', value=10, weight=5),
            Item(name='laptop', value=40, weight=4),
            Item(name='stereo', value=30, weight=6),
        ]
        for _ in range(1000):
            random.shuffle(items)
            self.assertEqual(effective_solution.solve(10, items), 90)
            self.assertEqual(brutal_solution.solve(10, items), 90)

    def test_random_values(self):
        """Tests random bags and items."""
        for _ in range(1000):
            items = []
            for i in range(8):
                value = random.randint(100, 300)
                items.append(
                    Item(
                        name=f'item: {i}',
                        value=value,
                        weight=random.randint(2, 20)
                    )
                )
            max_weight = 100
            c1 = effective_solution.solve(max_weight=max_weight, items=items)
            c2 = brutal_solution.solve(max_weight=max_weight, items=items)
            self.assertEqual(c1, c2)


if __name__ == '__main__':
    unittest.main()
