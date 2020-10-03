"""Implements the dynamic programming solution to the knapsack problem."""

import numpy as np


def solve(max_weight, items):
    """Efficient knapsack solution complexity: O(nm).

    Complexity is: O(nm) where n: the number of items and m the max_weight.

    :param int max_weight: The maximum weight that the bug can carry.
    :param list items: A list of objects exposing a value and weight attributes.

    :returns: The maximum value consisting of items whose total weight
    is less than the passed-in maximum weight.
    """
    items = sorted(items, key=lambda x: x.weight)
    values = np.zeros((len(items), max_weight))
    for item_index, item in enumerate(items):
        for j in range(max_weight):
            current_max_weight = j + 1
            if item_index == 0:
                if current_max_weight >= item.weight:
                    values[item_index, j] = item.value
            elif current_max_weight < item.weight:
                values[item_index, j] = values[item_index - 1, j]
            elif int(current_max_weight) == int(item.weight):
                values[item_index, j] = int(
                    max(values[item_index - 1, j], item.value))
            else:
                d = current_max_weight - item.weight
                assert d > 0
                v2 = item.value + int(values[item_index - 1, d - 1])
                values[item_index, j] = int(max(values[item_index - 1, j], v2))
    return values[-1, -1]
