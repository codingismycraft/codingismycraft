"""Solves the remove islands problem."""


def remove_islands(input):
    """Solves the remove islands problems.

    The logic goes as follows:

    - Convert the passed in matrix to a graph.
    - Discover all the bordering nodes with a value 1.
    - For each bordering node find all of its connected nodes.
    - Reformat the passed-in matrix using only connected nodes.

    :param list[list] input: The matrix representing the islands as 0 and 1.

    :return: A matrix removing the non connected to the board islands.
    :rtype: list[list]
    """
    g = _make_graph_from_adjacency_list(input)
    border_nodes = _get_borders(matrix=input)
    connected = []
    for node in border_nodes:
        connected.extend(_find_connected_subgraph(g, node))
    connected = set(connected)
    num_rows = len(input)
    num_cols = len(input[0])

    solution = []
    for row in range(num_rows):
        line = []
        for column in range(num_cols):
            if input[row][column] == 0:
                line.append(0)
            else:
                if _make_name(row, column) in connected:
                    line.append(1)
                else:
                    line.append(0)
        solution.append(line)
    return solution


def _make_name(row_index, col_index):
    """Converts the pair of row - col index to a name.

    :param int row_index: The row index.
    :param int col_index: The col index.

    :return: A name representing the passed in row-index pair.
    :rtype: str
    """
    return f'{col_index}:{row_index}'


def _get_borders(matrix):
    """Returns the external nodes for the passed in matrix.

    :param list[list] input: The matrix representing the islands as 0 and 1.

    :return: The external nodes for the passed in matrix.
    :rtype: list
    """
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    borders = []
    for row in [0, num_rows - 1]:
        for column in range(num_cols):
            if matrix[row][column] == 0:
                continue
            borders.append(_make_name(row, column))

    for row in range(num_rows):
        for column in [0, num_cols - 1]:
            if matrix[row][column] == 0:
                continue
            name = _make_name(row, column)
            if name not in borders:
                borders.append(_make_name(row, column))

    return borders


def _add_to_graph(g, item1, item2):
    """Adds the passed in pair of items to the graph.

    :param dict g: The graph to update.
    :param item1: The item to add to the graph.
    :param item2: The item to add to item1.
    """
    if item1 not in g:
        g[item1] = set()
    g[item1].add(item2)


def _make_graph_from_adjacency_list(matrix):
    """Converts the passed in matrix to a graph.

    :param list[list] matrix: The matrix representing the islands as 0 and 1.

    :return: The corresponding graph as a dict.
    :rtype: dict.
    """
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    adjacent_pairs = []
    graph = {}
    for row in range(0, num_rows):
        for column in range(0, num_cols):
            if matrix[row][column] == 0:
                continue

            connected_items = []

            # Add the "up" item.
            if row >= 1 and matrix[row - 1][column] == 1:
                assert row - 1 >= 0
                connected_items.append(_make_name(row - 1, column))

            # Add the "down" item.
            if row < num_rows - 1 and matrix[row + 1][column] == 1:
                assert row + 1 < num_rows
                connected_items.append(_make_name(row + 1, column))

            # Add the "left" item.
            if column >= 1 and matrix[row][column - 1] == 1:
                assert column - 1 >= 0
                connected_items.append(_make_name(row, column - 1))

            # Add the "right" item.
            if column < num_rows - 1 and matrix[row][column + 1] == 1:
                assert column + 1 < num_rows
                connected_items.append(_make_name(row, column + 1))

            this_item = _make_name(row, column)

            if not connected_items:
                graph[this_item] = set()

            for item in connected_items:
                adjacent_pairs.append((this_item, item))

    for item1, item2 in adjacent_pairs:
        _add_to_graph(graph, item1, item2)
        _add_to_graph(graph, item2, item1)
    return graph


def _find_connected_subgraph(g, node):
    """Returns the connected sub-graph for the passed in node.

    :param dict g: The full graph to extract the connected nodes from.
    :param node: The node to get its connected nodes.

    :return: The connected nodes as a list.
    :rtype: list
    """
    visited = set()
    queue = [node]
    while queue:
        current = queue.pop(0)
        visited.add(current)
        for child in g[current]:
            if child not in visited:
                queue.append(child)
    return list(visited)
