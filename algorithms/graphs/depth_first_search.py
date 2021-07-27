"""Implements depth first search."""


def dfs(graph, parent):
    assert parent in graph
    visited = []
    stack = []
    path = []
    while parent:
        if parent not in visited:
            visited.append(parent)
        path.append(parent)
        print(f'parent: {parent}  stack: {stack}')
        new_parent = get_unvisited_child(graph, parent, visited)
        if new_parent:
            stack.append(parent)
        elif not new_parent and stack:
            new_parent = stack.pop()
        parent = new_parent
    return visited, path


def get_unvisited_child(graph, parent, visited):
    for child in graph[parent]:
        if child not in visited:
            return child
    return None


def find_path(graph, parent, destination):
    assert parent in graph
    visited = []
    stack = []
    path = []
    while parent:
        if parent not in visited:
            visited.append(parent)
        path.append(parent)
        if parent == destination:
            return path
        new_parent = get_unvisited_child(graph, parent, visited)
        if new_parent:
            stack.append(parent)
        elif not new_parent and stack:
            new_parent = stack.pop()
        parent = new_parent
    return path
