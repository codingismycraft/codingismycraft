"""Exposes the topological sort algorithm."""

import random


def top_sort(graph):
    """Top-sorts the passed in DAG graph.

    :param dict graph: The DAG graph as an adjacent list.

    :return: A list expressing a topological sort of the passed in graph.
    :rtype: list
    """
    available_nodes = list(graph.keys())
    random.shuffle(available_nodes)
    completed = []

    while available_nodes:
        current_node = available_nodes.pop()
        explore(current_node, graph, completed)

    return list(reversed(completed))


def explore(node, graph, completed):
    """Explores the passed in node.

    :param node: The node to explore.
    :param dict graph: The DAG graph as an adjacent list.
    :param list completed: A list containing the explored nodes.
    """
    if node not in completed:
        for child in graph[node]:
            if child not in completed:
                explore(child, graph, completed)
        completed.append(node)
