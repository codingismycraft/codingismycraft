import bfs
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

if __name__ == '__main__':
    g = Graph(data)
    retrieved = bfs.bsf(g, '9', '3')
    utils.display_graph(
        g.get_as_dict(),
        retrieved,
        edgewidth=4,
        node_size=800,
        alpha=1
    )
