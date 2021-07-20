"""Exposes graph utilities."""

import matplotlib.pyplot as plt
import networkx as nx


def display_graph(data, path=None):
    """Displays the passed in graph and path."""
    edges = []
    for k, v in data.items():
        for v1 in v:
            edges.append((k, v1))

    G = nx.Graph(data)
    pos = nx.spring_layout(G)  # positions for all nodes

    # nodes
    options = {"node_size": 500, "alpha": 0.8}
    nx.draw_networkx_nodes(
        G,
        pos,
        nodelist=list(data.keys()),
        node_color="c",
        **options
    )

    # edges
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=edges,
        width=8,
        alpha=0.5,
        edge_color="b",
    )

    if path:
        nx.draw_networkx_edges(
            G,
            pos,
            edgelist=path,
            width=8,
            alpha=0.5,
            edge_color="r",
        )

    labels = {k: k for k in data}
    nx.draw_networkx_labels(G, pos, labels, font_size=16)

    plt.axis("off")
    plt.show()


if __name__ == '__main__':
    data = {
        '5': ['3', '7'],
        '3': ['2', '4'],
        '7': ['8'],
        '2': [],
        '4': ['8'],
        '8': []
    }
    path = [("5", "3"), ("3", "2")]
    display_graph(data, path=path)
