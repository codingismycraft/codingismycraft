"""Tests the in order successor in a Binary Search Tree algorithm."""

import random

import bst


def test_creation():
    """Tests the creation of a BST."""
    node = bst.Node(10)
    assert node.left_value is None
    assert node.right_value is None

    node.add_value(8)

    node.add_value(9)
    node.add_value(1)

    assert node.left_value == 8
    assert node.right_value is None

    node.add_value(100)
    assert node.left_value == 8
    assert node.right_value == 100

    node.add_value(99)


def test_successor_of_single_node():
    node = bst.Node(10)
    assert node.in_order_successor(10) is None
    assert node.in_order_successor(1) is None
    assert node.in_order_successor(11) is None


def test_no_right_branch():
    node = bst.Node(10)
    assert node.in_order_successor(10) is None

    node.add_value(8)
    assert node.in_order_successor(10) is None

    node.add_value(9)
    node.add_value(1)

    assert node.in_order_successor(10) is None


def test_using_last_left():
    node = bst.Node(10)
    node.add_value(8)
    node.add_value(9)
    node.add_value(1)

    assert node.in_order_successor(9) == 10


def test_using_right_branch():
    node = bst.Node(10)
    node.add_value(8)
    node.add_value(9)
    node.add_value(1)

    assert node.in_order_successor(8) == 9
    assert node.in_order_successor(1) == 8


def test_random_sample():
    count = 1000
    values = [random.randint(0, 10000) for _ in range(count)]
    values = list(set(values))
    sorted_values = sorted(values)

    random.shuffle(values)
    node = bst.Node(values.pop())
    for v in values:
        node.add_value(v)

    for index, v in enumerate(sorted_values[:-1]):
        assert node.in_order_successor(v) == sorted_values[index + 1]
