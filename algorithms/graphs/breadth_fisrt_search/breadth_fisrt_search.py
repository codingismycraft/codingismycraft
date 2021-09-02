"""Trivial Breadth-first search implementation."""


def bsf(graph, root, destination):
    """Uses bsf to find the path from root to destination.

    :param dict g : The graph to search.
    :param root : The root to start from.
    :param destination : The node to end.

    :returns: The shortest path from root to destination.
    :rtype: list
    """
    queue = [(root, [root])]
    visited = {root}
    while queue:
        parent, path = queue.pop(0)
        if parent == destination:
            return path
        for child in graph[parent]:
            if child not in visited:
                visited.add(child)
                queue.append((child, path[:] + [child]))
    return []
