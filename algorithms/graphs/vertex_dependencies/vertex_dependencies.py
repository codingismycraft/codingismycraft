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
        print(f"Counting dependencies for {node}")
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
    dependency_counter = {parent: 0 for parent in graph}
    for current_node in graph:
        stack = [[current_node, iter(graph[current_node])]]
        visited = set()
        visited.add(current_node)
        while stack:
            parent, children_iter = stack[-1]
            try:
                child = next(children_iter)
                if child not in visited:
                    visited.add(child)
                    dependency_counter[current_node] += 1
                    stack.append([child, iter(graph[child])])
            except StopIteration:
                stack.pop()
    return dependency_counter
