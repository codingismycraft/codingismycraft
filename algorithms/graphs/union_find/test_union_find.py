"""Tests union find."""

import unittest

import unionfind


class MyUnionFind(unittest.TestCase):
    def test_disjoint_set(self):
        """Tests the disjoint set function."""
        graph = {
            "A": ["B", "C"],
            "B": ["A", "D", "E"],
            "C": ["A", "D"],
            "D": ["B", "C"],
            "E": ["B", "G", "F"],
            "F": ["E", "H"],
            "G": ["E", "H"],
            "H": ["G", "F"],
        }

        retrieved = unionfind.disjoint(graph)
        print(retrieved)
        self.assertEqual(len(retrieved), 7)

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

        cycle_finder = unionfind.CycleFinder()

        no_cycle_forming_edges = []
        for n1, n2 in edges:
            if cycle_finder.is_cycle(n1, n2):
                print(f"{n1}, {n2} are forming a cycle..")
            else:
                no_cycle_forming_edges.append( (n1, n2) )

        print(no_cycle_forming_edges)





if __name__ == '__main__':
    unittest.main()
