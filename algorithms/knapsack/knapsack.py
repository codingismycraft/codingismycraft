"""Implements a dynamic programming solution to the knapsack problem."""


class Item:
    """Holds the data for an item that will be inserted in the knapsack.

    :ivar int w: The weight of the item.
    :ivar int v: The value of the item.
    """

    def __init__(self, w, v):
        """Initializer.

        :param int w: The weight of the item.
        :param int v: The value of the item.
        """
        self.w = w
        self.v = v

    def __repr__(self):
        return f'Item(weight={self.w}, value={self.v})'


def solve_bags(weights, values, max_capacity):
    """Solves the knapsack problem for the passed in parameters.

    :param list [int] weights: The weights of the available items.
    :param list [int] values: The weights of the available values.
    :param int max_capacity: The maximum weight the bag can carry.

    :return: A tuple of the maximum value and a list of the corresponding items.
    :rtype: tuple [int, list[Item] ]
    """
    # Add a dummy zero weight item.
    weights.append(0)
    values.append(0)

    # Make a list of items.
    items = [Item(w, v) for w, v in zip(weights, values)]

    # Sort items.
    items.sort(key=lambda item: item.w)

    # Create bags.
    bags = [[0] * (max_capacity + 1) for _ in range(0, len(items))]

    # Update values.
    for row_index in range(1, len(items)):
        for col_index in range(1, max_capacity + 1):
            if items[row_index].w > col_index:
                bags[row_index][col_index] = bags[row_index - 1][col_index]
            else:
                leftover_capacity = col_index - items[row_index].w
                v1 = items[row_index].v + bags[row_index - 1][leftover_capacity]
                bags[row_index][col_index] = max(v1,
                                                 bags[row_index - 1][col_index])

    selected_items = _get_selected_items(bags, items)

    return bags[-1][-1], selected_items


def _get_selected_items(bags, items):
    """Discovers the selected items from a solved array.

    :param list [ list[int]] bags: A two dimensional array holding the values
    for the knapsack solution.

    :param list [Items] items: A list holding the available items.
    :rtype:list[Item]
    """
    if not bags:
        return []

    number_of_rows = len(bags)
    number_of_cols = len(bags[0])

    value = bags[number_of_rows - 1][number_of_cols - 1]

    row_index = number_of_rows - 1
    col_index = number_of_cols - 1

    selected_indexes = []
    total_selected_weight = 0
    while row_index > 0 and total_selected_weight < value:
        v1 = bags[row_index - 1][col_index]
        if v1 == bags[row_index][col_index]:
            row_index -= 1
        else:
            total_selected_weight += items[row_index].w
            selected_indexes.append(row_index)
            col_index = col_index - items[row_index].w
            row_index -= 1
    selected_items = []
    for i in sorted(selected_indexes):
        selected_items.append(items[i])
    return selected_items
