"""Tests the cycles in the linked list cycles."""

import unittest
import llc

# Aliases.
Node = llc.Node


class TestLinkedListCycles(unittest.TestCase):
    """Test the detection of a cycle in a linked list."""

    def test_cycle_detection(self):
        """The the has_cycle detection logic."""
        root = Node('a')
        n1 = root.add("b")
        n2 = root.add("c")
        self.assertFalse(root.has_cycle())

        n2.set_next(n1)
        self.assertTrue(root.has_cycle())


if __name__ == '__main__':
    unittest.main()
