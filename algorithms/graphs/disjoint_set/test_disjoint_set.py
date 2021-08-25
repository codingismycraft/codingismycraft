"""Tests the brutal_disjoint_set module.

To better understand the data and the algorithm see brutal-disjoint-set.png.
"""

import unittest

import disjoint_set


class TestBrutalDisjointSet(unittest.TestCase):
    """Test the brutal_disjoint_set function."""

    def test_brutal_disjoint_set(self):
        """Test the brutal_disjoint_set function."""
        edges = [
            ('A', 'B'),
            ('A', 'C'),
            ('C', 'D'),
            ('D', 'B'),
            ('B', 'C'),
            ('D', 'E'),
        ]
        expected = [('A', 'C'), ('C', 'D'), ('D', 'E'), ('A', 'B')]

        retrieved = disjoint_set.brutal_disjoint_set(edges)
        self.assertListEqual(sorted(expected), sorted(retrieved))


class TestEfficientDisjointSet(unittest.TestCase):
    """Tests the efficient disjoint set."""

    def test_count_disjoint_sets(self):
        edges = [
            ('A', 'B'),
            ('A', 'C'),
            ('C', 'D'),
            ('D', 'B'),
            ('B', 'C'),
            ('D', 'E'),
        ]

        ds = disjoint_set.DisjointSet()
        for n1, n2 in edges:
            ds.union(n1, n2)
            self.assertEqual(ds.count_disjoint_sets(), 1)
        self.assertEqual(ds.count_disjoint_sets(), 1)

        ds.union('Z', 'Y')
        ds.union('Z', 'X')
        ds.union('Y', 'X')
        self.assertEqual(ds.count_disjoint_sets(), 2)

        ds.union('ZZ', 'YY')
        self.assertEqual(ds.count_disjoint_sets(), 3)

    def test_disjoint_set(self):
        ds = disjoint_set.DisjointSet()
        retrieved = ds.union('A', 'B')
        self.assertTrue(retrieved)
        self.assertEqual(len(ds._nodes), 2)
        self.assertEqual(ds._nodes['A'], 2)
        self.assertEqual(ds._nodes['B'], 'A')

        retrieved = ds.union('A', 'C')
        self.assertTrue(retrieved)
        self.assertEqual(len(ds._nodes), 3)
        self.assertEqual(ds._nodes['A'], 3)
        self.assertEqual(ds._nodes['B'], 'A')
        self.assertEqual(ds._nodes['C'], 'A')

        retrieved = ds.union('C', 'D')
        self.assertTrue(retrieved)

        retrieved = ds.union('B', 'D')
        self.assertFalse(retrieved)

        retrieved = ds.union('B', 'C')
        self.assertFalse(retrieved)

        retrieved = ds.union('D', 'E')
        self.assertTrue(retrieved)

        self.assertTrue(ds.check_cycle('B', 'C'))
        self.assertTrue(ds.check_cycle('B', 'E'))
        self.assertFalse(ds.check_cycle('F', 'E'))


if __name__ == '__main__':
    unittest.main()
