"""Trivial Breadth-first search implementation."""


def get_bsf_spanning_tree(g, root):
    """Finds the spanning tree for the passed in graph.

    :param Graph g : The graph to search.
    :param root : The root Node.

    :returns: The spanning tree as a list for the whole graph.
    :rtype: list
    """
    visited = []
    nodes = [root]
    spanning_tree = []

    while nodes:
        current_node = nodes.pop(0)
        if current_node in visited:
            continue
        spanning_tree.append(current_node)
        visited.append(current_node)
        for child in g.get_children(current_node):
            if child not in visited:
                nodes.append(child)

    return spanning_tree


def bsf(g, root, destination):
    """Uses bsf to find the path from root to destination.

    :param Graph g : The graph to search.
    :param root : The root to start from.
    :param destination : The node to end.

    :returns: The shortest path from root to destination.
    :rtype: list
    """
    visited = []
    nodes = [(root, [root])]

    while nodes:
        current_node, path = nodes.pop(0)
        if current_node in visited:
            continue

        visited.append(current_node)
        for child in g.get_children(current_node):
            if child not in visited:
                path1 = path[:]
                path1.append(child)
                if child == destination:
                    return _make_path(path1)
                else:
                    nodes.append((child, path1))

    return []


def _make_path(path):
    """Creates a path in the form of [ (x1,x2), (x2, x3) .. ].

    :param list path: A list of nodes.

    :return: A list in the form of [ (x1,x2), (x2, x3) .. ].
    :rtype: list [tuple]
    """
    if not path or len(path) == 1:
        return []

    p = []
    c1 = path.pop()
    while path:
        c2 = path.pop()
        p.append((c1, c2))
        c1 = c2
    return p
