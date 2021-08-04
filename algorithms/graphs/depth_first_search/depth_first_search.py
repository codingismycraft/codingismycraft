"""Implements depth first search."""


def dfs(graph, parent, destination=None):
    """Traverses the passed in graph using depth first search.

    1. Create a stack to hold the previously visited nodes.
    2. Create a set holding the visited notes.
    3. For the current parent:
        - Add it to the visited set.
        - Find the next unvisited child for the parent.
        - If an unvisited child was found add the parent to the stack and
          make the child the parent
        - Else if there are nodes it the stack pop the next parent from there
         else we are done.

    :param dict graph: An adjacency list representation of the graph.
    :param parent: The parent node.
    :param destination: The destination node; if None then the whole graph
        will be traversed.

    :return: A tuple consisting of the visited nodes and the path.
    :rtype: tuple [list, list]
    """
    nodes = []
    visited = set()
    path = []
    all_steps = []
    while parent:
        print(parent, nodes)
        all_steps.append(parent)
        if parent not in visited:
            path.append(parent)
        visited.add(parent)
        next_parent = get_unvisited_child(graph, parent, visited)
        if next_parent is not None:
            nodes.append(parent)
        elif nodes:
            next_parent = nodes.pop()
        parent = next_parent
    return visited, path, all_steps


def get_unvisited_child(graph, node, visited):
    for child in graph[node]:
        if child not in visited:
            return child
    return None
