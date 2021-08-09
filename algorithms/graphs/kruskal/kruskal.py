"""Implements the Kruskal's min path Spanning tree."""


class DisjointSet:
    """Implements disjoint set.

    :ivar dict _nodes: Holds a dict from the node name to its parent or if
    it is a root to the number of its children (including self).
    """

    def __init__(self):
        """Initializer."""
        self._nodes = {}

    def check_cycle(self, node1, node2):
        """Checks is adding the passed in edge will form an edge.

        :param node1: The first node of the edge to check.
        :param node2: The second node of the edge to check.

        :return: True if adding the edge will form a cycle.
        :rtype: bool
        """
        return self._find_parent(node1) == self._find_parent(node2)

    def count_disjoint_sets(self):
        """Counts the number of disjoint sets.

        :return: The number of disjoint sets.
        :rtype: int
        """
        count = 0
        for value in self._nodes.values():
            if isinstance(value, int):
                count += 1
        return count

    def union(self, node1, node2):
        """Unions the passed in edge if no cycle is created.

        :param node1: The first node of the edge to add.
        :param node2: The second node of the edge to add.

        :return: True if adding the edge was added.
        :rtype: bool
        """
        p1 = self._find_parent(node1)
        p2 = self._find_parent(node2)

        if p1 == p2:
            return False  # Forms a cycle.

        # The parent will be the "heavier" node.
        if self._nodes[p1] >= self._nodes[p2]:
            parent = p1
            child = p2
        else:
            parent = p2
            child = p1

        # Union them.
        self._nodes[parent] += self._nodes[child]
        self._nodes[child] = parent

        return True

    def _find_parent(self, node):
        """Finds the parent node for the passed in node.

        If the node does not exist it is created.

        :param node: The node to lookup.

        :return: The parent node of the passed in node.
        :rtype: node
        """
        if node not in self._nodes:
            self._nodes[node] = 1
            return node
        elif isinstance(self._nodes[node], int):
            return node
        else:
            return self._find_parent(self._nodes[node])


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

    ds = DisjointSet()
    path = []
    total_weight = 0
    for (node1, node2), weight in edges:
        if ds.union(node1, node2):
            path.append([node1, node2])
            total_weight += weight
    return path, total_weight



