class Item:
    def __init__(self, w, v):
        self.w = w
        self.v = v

    def __repr__(self):
        return f'Item({self.w, self.v})'


def solve_bags(weights, values, max_capacity):
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
        for col_index in range(1, max_capacity+1):
            if items[row_index].w > col_index:
                bags[row_index][col_index] = bags[row_index-1][col_index]
            else:
                leftover_capacity = col_index - items[row_index].w
                v1 = items[row_index].v + bags[row_index-1][leftover_capacity]
                bags[row_index][col_index] = max(v1, bags[row_index-1][col_index])

    return bags[-1][-1]
