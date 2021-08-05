"""Finds the path in a maze."""

_GRAPH_MATRIX = [
    [0, 1, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0],
    [1, 0, 0, 1, 1, 0, 1, 0],
    [1, 1, 0, 1, 1, 0, 1, 0],
    [1, 0, 1, 1, 1, 0, 1, 0],
    [1, 1, 1, 0, 1, 1, 1, 0],
    [1, 1, 0, 0, 0, 0, 1, 0],
    [1, 1, 1, 0, 1, 1, 1, 1]
]


def make_name(row_index, col_index):
    return f'{row_index}:{col_index}'


def add_to_graph(g, item1, item2):
    if item1 not in g:
        g[item1] = set()
    g[item1].add(item2)


def make_graph(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    adjacent_pairs = []

    for row in range(0, num_rows):
        for column in range(0, num_cols):
            if matrix[row][column] == 0:
                continue

            connected_items = []

            # Add the "up" item.
            if row >= 1 and matrix[row - 1][column] == 1:
                assert row - 1 >= 0
                connected_items.append(make_name(row - 1, column))

            # Add the "down" item.
            if row < num_rows - 1 and matrix[row + 1][column] == 1:
                assert row + 1 < num_rows
                connected_items.append(make_name(row + 1, column))

            # Add the "left" item.
            if column >= 1 and matrix[row][column - 1] == 1:
                assert column - 1 >= 0
                connected_items.append(make_name(row, column - 1))

            # Add the "right" item.
            if column < num_rows - 1 and matrix[row][column + 1] == 1:
                assert column + 1 < num_rows
                connected_items.append(make_name(row, column + 1))

            this_item = make_name(row, column)
            for item in connected_items:
                adjacent_pairs.append((this_item, item))

    graph = {}
    for item1, item2 in adjacent_pairs:
        add_to_graph(graph, item1, item2)
        add_to_graph(graph, item2, item1)
    return graph


def bsf(graph, root, destination):
    """Uses bsf to find the path from root to destination.

    :param dict g : The graph to search.
    :param root : The root to start from.
    :param destination : The node to end.

    :returns: The shortest path from root to destination.
    :rtype: list
    """
    if root not in graph or destination not in graph:
        return []

    visited = [root]
    queue = [(root, [root])]

    while queue:
        node, path = queue.pop(0)
        if node == destination:
            return path
        visited.append(node)
        for child in graph[node]:
            if child not in visited:
                queue.append( (child, path[:] + [child]))

    return []



g = make_graph(_GRAPH_MATRIX)

for k, v in g.items():
    print(k, v)



print("using breadth first search")
retrieved = bsf(g, "7:0", "0:7")
print(retrieved)

# path = [x[0] for x in retrieved]
# print(path)
# print("using depth first search")
# print(depth_first_search.dfs(Graph.get_as_dict(), "7:0", "0:7")[1])
