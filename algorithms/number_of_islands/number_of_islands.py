"""Solves the number of islands.

See also https://leetcode.com/problems/number-of-islands/
"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        graph = _make_graph_from_adjacency_list(grid)
        counter = 0
        while graph:
            node = list(graph.keys())[0]
            subgraph = _find_connected_subgraph(graph, node)
            counter += 1
            for n in subgraph:
                del graph[n]
        return counter


def _make_name(row_index, col_index):
    """Converts the pair of row - col index to a name.

    :param int row_index: The row index.
    :param int col_index: The col index.

    :return: A name representing the passed in row-index pair.
    :rtype: str
    """
    return f'{col_index}:{row_index}'


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
            if matrix[row][column] == "0":
                continue

            connected_items = []

            # Add the "up" item.
            if row >= 1 and matrix[row - 1][column] == "1":
                assert row - 1 >= 0
                connected_items.append(_make_name(row - 1, column))

            # Add the "down" item.
            if row < num_rows - 2 and matrix[row + 1][column] == "1":
                assert row + 1 < num_rows
                connected_items.append(_make_name(row + 1, column))

            # Add the "left" item.
            if column >= 1 and matrix[row][column - 1] == "1":
                assert column - 1 >= 0
                connected_items.append(_make_name(row, column - 1))

            # Add the "right" item.
            if column < num_cols - 2 and matrix[row][column + 1] == "1":
                assert column + 1 < num_cols
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
