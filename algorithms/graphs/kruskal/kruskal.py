"""Implements the Kruskal's min path Spanning tree."""




def kruskal(graph):
    """Find the minimum spanning tree using Kruskal's algorithm.

    :param dict graph: The graph passed as a dictionary.

    :return: The minimum spanning tree as a list of tuple.
    :rtype: tuple
    """
    edges = set()
    for node1, children in graph.items():
        for node2, weight in children:
            n1, n2 = node1, node2
            if n1 > n2:
                n1, n2 = n2, n1
            edges.add(((n1, n2), weight))
    edges = list(edges)
    edges.sort(key=lambda x: x[1])

    cd = _CycleDetector()
    path = []
    total_weight = 0
    for (node1, node2), weight in edges:
        if not cd.forms_cycle(node1, node2):
            path.append([node1, node2])
            total_weight += weight
    return path, total_weight




class _CycleDetector:
    def __init__(self):
        self._parents = {}

    def forms_cycle(self, n1, n2):
        self._add_nodes_if_needed(n1, n2)

        p1 = self._get_top_level_parent(n1)
        p2 = self._get_top_level_parent(n2)

        if p1 == p2:
            return True

        assert self.is_top_level_parent(p1)
        assert self.is_top_level_parent(p2)

        size_1 = self._parents[p1]
        size_2 = self._parents[p2]

        if size_1 < size_2:
            p1, p2 = p2, p1
            n1, n2 = n2, n1

        self._parents[p1] += size_2

        self._parents[p2] = p1
        self._parents[n2] = p1

        return False

    @property
    def parents(self):
        return self._parents.copy()

    def is_top_level_parent(self, node):
        assert node in self._parents
        return isinstance(self._parents[node], int)

    def _add_nodes_if_needed(self, *nodes):
        for node in nodes:
            assert not isinstance(node, int)
            if node not in self._parents:
                self._parents[node] = 1

    def _get_top_level_parent(self, node):
        assert node in self._parents
        if self.is_top_level_parent(node):
            return node
        else:
            return self._get_top_level_parent(self._parents[node])

