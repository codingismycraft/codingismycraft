def find_shortest_path(g, start_node, end_node):
    queue = [(start_node, [start_node])]
    visited = []

    while queue:
        current_node = queue.pop(0)
        visited.append(current_node[0])
        if current_node[0] == end_node:
            return current_node[1]
        for child_node in g[current_node[0]]:
            if child_node not in visited:
                queue.append((child_node, current_node[1] + [child_node]))

    return False
