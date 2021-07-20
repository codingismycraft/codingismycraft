"""Trivial graph implementation."""


class Graph:
    def __init__(self, data=None):
        """Initializer.

        :param dict data: The graph as a dict.
        """
        if not data:
            data = {}
        self._graph = {}

        for k, v in data.items():
            for n in v:
                self.add_edge(n, k)

    def __repr__(self):
        """Get a simple instance description to use for debugging.

        :return: A simple instance description to use for debugging.
        :rtype: str.
        """
        return f'Graph: Number of nodes {len(self._graph)}'

    def get_as_dict(self):
        """Returns the graph as dict.

        :return: The graph as dict.
        :rtype: dict
        """
        return self._graph.copy()

    def __str__(self):
        """Returns the graph as a string.

        :return: The graph as a string.
        :rtype: str.
        """
        lines = []
        for n in list(self._graph.keys()):
            connected_nodes = ' - '.join([str(x) for x in self.get_edges(n)])
            lines.append(f'{n}: {connected_nodes}')
        return '\n'.join(lines)

    def __contains__(self, v):
        """Checks if the passed in value is a vertex..

        :param v: The value to check.

        :return: True if the passed in value is a vertex.
        :rtype: bool.
        """
        return v in self._graph

    def get_children(self, value):
        """Iterates through all the connected nodes for the passed in value

        :param value: The node value to return its connections.

        :returns: An iterator to all connected nodes for the passed in value.
        :rtype: iter
        """
        return iter(self._graph.get(value))

    def get_edges(self, v):
        """Gets all the edges for the passed in value.

        :return: A set with the connected to v nodes.
        :rtype: set.
        """
        if v not in self:
            raise ValueError(f'Node: {v} does not exist')
        return self._graph.get(v)

    def add_node(self, value):
        """Adds a node if not already existing.

        :param value: The value of the node to add.
        """
        if value not in self:
            self._graph[value] = set()
            return True
        return False

    def add_edge(self, v1, v2):
        """Adds an edge.

        :param v1: The value of the first node to add.
        :param v2: The value of the second node to add.
        """
        if v1 not in self:
            self.add_node(v1)
        if v2 not in self:
            self.add_node(v2)
        if v2 not in self._graph[v1]:
            self._graph[v1].add(v2)
        if v1 not in self._graph[v2]:
            self._graph[v2].add(v1)
