"""Iterates a graph assigning the total number of dependencies to each node."""

import functools


class DependencyCounter:
    def __init__(self, graph):
        self._graph = graph

    @functools.lru_cache()
    def _get_dependencies(self, node):
        """Counts the dependencies for the passed in node.

        :param str node: The node to count dependencies for.

        :returns: All the dependencies for the passed in node.
        :rtype: set.
        """
        dependencies = set()
        for child in self._graph[node]:
            dependencies.add(child)
            dependencies.update(self._get_dependencies(child))
        return dependencies

    @classmethod
    def count_dependencies(cls, graph):
        """Counts the total number of dependencies for each vertex."

        :param dict graph: The graph to use.

        :returns: A dict from the vertex to the total dependency count.
        :rtype: dict[str, int].
        """
        graph = graph.copy()
        dc = cls(graph)

        dependency_count = {
            node: len(dc._get_dependencies(node))
            for node in graph
        }

        return dependency_count
