"""Tests the brutal_disjoint_set module.

To better understand the data and the algorithm see brutal-disjoint-set.png.
"""

import unittest

import brutal_disjoint_set


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

        retrieved = brutal_disjoint_set.brutal_disjoint_set(edges)


if __name__ == '__main__':
    unittest.main()
