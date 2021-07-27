import random

import breadth_fisrt_search as bfs
import graph
import utils

# Aliases.
Graph = graph.Graph

# data = {
#     '5': ['3', '7', '1'],
#     '3': ['2', '4'],
#     '7': ['8', '5'],
#     '2': ['5'],
#     '4': ['8', '2'],
#     '8': ['5', '4'],
#     '1': ['2'],
#     '9': ['8']
# }

data = {
    '0': ['1', '2', '3'],
    '1': ['0', '3', '4', '2', '5'],
    '2': ['0', '2', '1'],
    '3': ['1', '0'],
    '4': ['2', '1'],
    '5': ['1']
}



def make_data():
    nodes = [str(i) for i in range(1, 16)]

    node_copy = nodes[:]

    g = {}
    for n in nodes:
        random.shuffle(node_copy)
        g[n] = node_copy[0:random.randint(0, 3)]

    return g


if __name__ == '__main__':
    # data = make_data()
    g = Graph(data)
    # retrieved = bfs.bsf(g, '3', '8')
    utils.display_graph(
        g.get_as_dict(),
        # retrieved,
        edgewidth=8,
        node_size=1000,
        alpha=1
    )
