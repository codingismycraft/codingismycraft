"""Brutal solution for knapsack problem,"""
import itertools


def solve(max_weight, items):
    """Brutal knapsack solution used for testing purposes, complexity: O(n!).

    :param int max_weight: The maximum weight that the bug can carry.
    :param list items: A list of objects exposing a value and weight attributes.

    :returns: The maximum value consisting of items whose total weight
    is less than the passed-in maximum weight.
    """
    power_set = list(itertools.chain.from_iterable(
        itertools.combinations(items, r) for r in range(len(items) + 1)
    ))
    max_value = 0
    for combo in power_set:
        if sum(item.weight for item in combo) <= max_weight:
            max_value = max(max_value, sum(item.value for item in combo))
    return max_value
