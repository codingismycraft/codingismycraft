# """"""
#
#
# def bfs(G, starting_node, ending_node,visited=None,queue=None):
#     """Return true if ending_node is found."""
#     if visited == None:
#         visited=[]
#     if queue==None:
#         queue=[(starting_node,[starting_node])]
#     children_of_current_node = G[starting_node]
#     for i in children_of_current_node:
#         if i not in visited:
#             if i==ending_node:
#                 return True
#             visited.append(i)
#             queue.append((i,[starting_node]+[i]))
#     if not queue:
#         return False
#     next_node=path[0]
#     return bfs(G,next_node,ending_node,visited,queue)
#
#
#


def bfs(G, starting_node, ending_node):
    queue = [(starting_node, [starting_node])]
    visited = []
    while queue:
        current_node = queue.pop(0)
        visited.append(current_node[0])
        if current_node[0]==ending_node:
            return current_node[1]
        for child in G[current_node[0]]:
            if child not in visited:
                queue.append((child,current_node[1]+[child]))
    return []

