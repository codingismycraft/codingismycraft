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


def count_dependencies(graph):
    nodes = list(graph.keys())
    dependencies = {}
    for node in nodes:
        _traverse_node(graph, node, dependencies)
    return {k: len(v) for k, v in dependencies.items()}


def _traverse_node(graph, node, dependencies):
    visited = set()
    stack = []
    current_node = node
    while current_node:
        if node not in dependencies:
            dependencies[node] = set()
        for child in graph[current_node]:
            dependencies[node].add(child)
        if current_node not in visited:
            visited.add(current_node)
        next_node = _get_unvisited_child(current_node, graph, visited)
        if next_node is not None:
            stack.append(current_node)
            current_node = next_node  # Move forward.
        elif stack:
            current_node = stack.pop()  # Move Backward.
        else:
            current_node = None
    return dependencies


def _get_unvisited_child(node, graph, visited):
    for child in graph[node]:
        if child not in visited:
            return child
    return None


