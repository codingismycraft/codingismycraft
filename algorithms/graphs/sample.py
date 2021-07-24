import random

import breadth_fisrt_search as bfs
import graph
import utils

# Aliases.
Graph = graph.Graph

data = {
    '5': ['3', '7', '1'],
    '3': ['2', '4'],
    '7': ['8', '5'],
    '2': ['5'],
    '4': ['8', '2'],
    '8': ['5', '4'],
    '1': ['2'],
    '9': ['8']
}

def make_data():
    nodes = [str(i) for i in range(1,16)]

    node_copy = nodes[:]

    g = {}
    for n in nodes:
        random.shuffle(node_copy)
        g[n] = node_copy[0:random.randint(0, 3)]

    return g


if __name__ == '__main__':
    data = make_data()
    g = Graph(data)
    retrieved = bfs.bsf(g, '3', '8')
    utils.display_graph(
        g.get_as_dict(),
        retrieved,
        edgewidth=2,
        node_size=180,
        alpha=1
    )
