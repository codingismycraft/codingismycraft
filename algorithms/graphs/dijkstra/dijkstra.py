"""Implements the dijkstra's algorithm."""

def evaluate(graph, starting_node):
    """Finds the shortest paths.

    :param dict graph: The weighted graph as an adjacent list.
    :param starting_node: The starting node.

    :return: A dict holding all the nodes of the graph pointing to
    their shortest distances from the starting node.
    :rtype dict.
    """
    distance_from_origin = {k: float('inf') for k in graph}
    distance_from_origin[starting_node] = 0
    queue = [starting_node]
    visited = []
    while queue:
        current_node = queue.pop(0)
        if current_node not in visited:
            for child, distance in graph[current_node]:
                d1 = distance + distance_from_origin[current_node]
                d2 = distance_from_origin[child]
                distance_from_origin[child] = min(d1, d2)
                queue.append(child)
        visited.append(current_node)
    return distance_from_origin
