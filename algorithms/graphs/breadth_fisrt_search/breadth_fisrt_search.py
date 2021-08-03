"""Trivial Breadth-first search implementation."""


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

