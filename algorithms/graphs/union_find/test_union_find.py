"""Tests union find."""

import random
import unittest

import unionfind


class MyUnionFind(unittest.TestCase):

    def test_check_cirle_forming(self):
        edges = [
            ('A', 'B'),
            ('A', 'C'),
            ('B', 'D'),
            ('B', 'E'),
            ('C', 'D'),
            ('E', 'G'),
            ('E', 'F'),
            ('F', 'H'),
            ('G', 'H')
        ]

        random.shuffle(edges)

        self.assertEqual(len(edges), 9)

        cycle_finder = unionfind.CycleFinder()
        no_cycle_forming_edges = []
        for n1, n2 in edges:
            if not cycle_finder.is_cycle(n1, n2):
                no_cycle_forming_edges.append((n1, n2))

        self.assertEqual(len(no_cycle_forming_edges), 7)
        print(no_cycle_forming_edges)
        print(cycle_finder.top_level_parents)

        # Verify compression
        # parents = cycle_finder.top_level_parents
        # for node, value in parents.items():
        #     if not isinstance(value, int):
        #         self.assertTrue(isinstance(parents[node], int))


if __name__ == '__main__':
    unittest.main()
