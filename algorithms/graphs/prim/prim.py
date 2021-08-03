"""Implements the prim algorithm to find minimum spanning tree."""


def _get_min_edge(graph):
    """Finds the minimum weighted edge for the passed in graph.

    :param dict graph: The weighted graph as an adjacent list.

    :return: The minimum weighted edge as a tuple of two nodes.
    :rtype: tuple
    """
    v = float('inf')
    min_edge = None
    for node_1, connected_nodes in graph.items():
        for node_2, value in connected_nodes:
            if value < v:
                min_edge = node_1, node_2
                v = value
    assert min_edge
    return min_edge


def merge(edges, index=0):
    """Transforms the passed in list of edges to become continued.

    :param list edges: A list ot edges in the form of [n1, n2]
    :param int index: The index of the first edge to use.

    :return: A continued versiion of the passed in edges.
    :rtype: list
    """
    if index >= len(edges) - 1:
        return edges
    else:
        e1 = edges[index]
        e2 = edges[index + 1]

        if e1[1] != e2[0]:
            e1[0], e1[1] = e1[1], e1[0]

        return merge(edges, index + 1)


def prim(graph):
    """Find the minimum spanning tree.

    :param dict graph: The graph passed as a dictionary.

    :return: The minimum spanning tree as a list of tuple.
    :rtype: tuple
    """
    min_edge = _get_min_edge(graph)
    node = min_edge[0]
    selected_edges = []
    path_nodes = [node]

    done = False
    total_weight = 0
    while not done:
        candidates = []
        for node in path_nodes:
            for child in graph[node]:
                name = child[0]
                weight = child[1]
                if name not in path_nodes:
                    candidates.append((node, name, weight))
        if candidates:
            candidates.sort(key=lambda x: x[2])
            top_candidate = candidates[0]
            selected_edges.append([top_candidate[0], top_candidate[1]])
            total_weight += top_candidate[2]
            path_nodes.append(top_candidate[1])
        else:
            done = True

    return merge(selected_edges), total_weight
