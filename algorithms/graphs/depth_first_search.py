"""Implements depth first search."""


def dfs(graph, parent, destination=None):
    """Traverses the passed in graph using depth first search.

    :param dict graph: An adjacency list representation of the graph.
    :param parent: The parent node.
    :param destination: The destination node; if None then the whole graph
        will be traversed.

    :return: A tuple consisting of the visited nodes and the path.
    :rtype: tuple [list, list]
    """
    assert parent in graph
    visited = set()
    stack = []
    path = []
    while parent:
        visited.add(parent)
        path.append(parent)
        if parent == destination:
            return visited, path
        new_parent = _get_unvisited_child(graph, parent, visited)
        if new_parent:
            stack.append(parent)  # Move forward.
        elif not new_parent and stack:
            new_parent = stack.pop()  # Go back.
        parent = new_parent
    return visited, path


def _get_unvisited_child(graph, parent, visited):
    """Finds an unvisited child for the passed in parent.

    :param dict graph: An adjacency list representation of the graph.
    :param parent: The parent node.
    :param set | list visited: The collection of the visited nodes.

    :returns: An unvisited child for the passed-in parent (or None if no
        unvisited nodes exist.
    """
    for child in graph[parent]:
        if child not in visited:
            return child
    return None
