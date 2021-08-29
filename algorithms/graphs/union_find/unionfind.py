import math


class CycleFinder:
    def __init__(self):
        self._top_level_parents = {}

    def is_cycle(self, n1, n2):
        if n1 not in self._top_level_parents:
            self._top_level_parents[n1] = -1

        if n2 not in self._top_level_parents:
            self._top_level_parents[n2] = -1

        p1 = self.find_top_level_parent(n1)
        p2 = self.find_top_level_parent(n2)

        if p1 == p2:
            return True

        size_1 = int(math.fabs(self._top_level_parents[p1]))
        size_2 = int(math.fabs(self._top_level_parents[p2]))

        if size_1 >= size_2:
            self._top_level_parents[p2] = p1
            self._top_level_parents[p1] -= size_2
        else:
            self._top_level_parents[p1] = p2
            self._top_level_parents[p2] -= size_1

        return False

    def find_top_level_parent(self, node):
        if isinstance(self._top_level_parents[node], int):
            return node
        else:
            return find_top_level_parent(self._top_level_parents,
                                         self._top_level_parents[node])


def disjoint(graph):
    """Returns a disjointed graph based on the passed in graph.

    :param dict graph: The graph to use.

    :returns: A disjoint graph.
    :rtype: dict
    """
    edges = []
    selected_edges = []
    for parent, children in graph.items():
        for child in children:
            if (child, parent) not in edges:
                edges.append((parent, child))

    top_level_parents = {parent: -1 for parent in graph}
    for n1, n2 in edges:
        p1 = find_top_level_parent(top_level_parents, n1)
        p2 = find_top_level_parent(top_level_parents, n2)

        if p1 == p2:
            continue

        selected_edges.append((n1, n2))

        size_1 = int(math.fabs(top_level_parents[p1]))
        size_2 = int(math.fabs(top_level_parents[p2]))

        if size_1 >= size_2:
            top_level_parents[p2] = p1
            top_level_parents[p1] -= size_2
        else:
            top_level_parents[p1] = p2
            top_level_parents[p2] -= size_1

    return selected_edges


def find_top_level_parent(top_level_parents, node):
    if isinstance(top_level_parents[node], int):
        return node
    else:
        return find_top_level_parent(top_level_parents, top_level_parents[node])
