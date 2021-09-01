class CycleFinder:
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

