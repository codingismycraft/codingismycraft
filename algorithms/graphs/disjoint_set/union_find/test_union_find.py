"""Tests union find."""

import random
import unittest

import unionfind


class MyUnionFind(unittest.TestCase):
    def test_check_cirle_forming1(self):
        cycle_finder = unionfind.CycleFinder()
        print(cycle_finder.parents)

        self.assertFalse(cycle_finder.forms_cycle("A", "B"))
        print(cycle_finder.parents)

        self.assertFalse(cycle_finder.forms_cycle("E", "D"))
        print(cycle_finder.parents)

        self.assertFalse(cycle_finder.forms_cycle("C", "D"))
        print(cycle_finder.parents)

        self.assertFalse(cycle_finder.forms_cycle("B", "C"))
        print(cycle_finder.parents)

        self.assertTrue(cycle_finder.forms_cycle("A", "D"))

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
            if not cycle_finder.forms_cycle(n1, n2):
                no_cycle_forming_edges.append((n1, n2))

        self.assertEqual(len(no_cycle_forming_edges), 7)
        print(no_cycle_forming_edges)
        print(cycle_finder.parents)


if __name__ == '__main__':
    unittest.main()
