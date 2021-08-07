"""Implements a brutal solution for the disjoint_set."""


def brutal_disjoint_set(edges):
    """Combines edges to a spanning tree with no cycles.

    :param list[tuple] edges: List of edges

    :return: A list of connected edges with no cycles.
    :rtype: list[tuple]
    """
    nodes = []
    for n1, n2 in edges:
        if n1 not in nodes:
            nodes.append(n1)
        if n2 not in nodes:
            nodes.append(n2)

    groups = {}
    for i, n in enumerate(nodes):
        groups[f'S{i+1}'] = [n]

    print(groups)

