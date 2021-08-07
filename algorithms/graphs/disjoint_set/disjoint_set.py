"""Implements a brutal solution for the disjoint_set."""


def brutal_disjoint_set(edges):
    """Implements a brutal solution for the disjoint_set.

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
    group_by_node = {}
    for i, n in enumerate(nodes):
        group_name = f'S{i+1}'
        groups[group_name] = [n]
        group_by_node[n] = group_name

    path = []
    for n1, n2 in edges:
        group_name_1 = group_by_node[n1]
        group_name_2 = group_by_node[n2]

        if group_name_1 != group_name_2:
            groups[group_name_1].extend(groups[group_name_2])
            del groups[group_name_2]
            group_by_node[n2] = group_name_1
            path.append((n1, n2))
    return path





