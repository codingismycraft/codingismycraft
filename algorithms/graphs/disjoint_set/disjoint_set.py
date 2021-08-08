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
        group_name = f'S{i + 1}'
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
