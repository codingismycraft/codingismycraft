# Graph definitions

### Undirected graph
Edges have no direction
### Directed graph
Edges have direction
### Adjacent vertices
In a graph G , two graph vertices are adjacent if they are joined by a graph edge
### Adjacent Edges
Adjacent edges are edges that share a common vertex
### Complete graph
Each vertex connect to each other vertex
### Simple graph
No loops and no parallel edges
### Cycle path
The only repeated vertices are the first and last vertices
### Subgraph
All of whose vertices and edges are contained in a larger graph
### Multi-graph
Can have more than one edge between a pair vertices.
### Self Loop
An edge of a graph which starts and ends at the same vertex
### Plannar graph
Can be drawn without any edges crossing
### Euclidean graph
A weighted graph in which the weights are equal to the Euclidean lengths of the edges in a specified embedding
### Isomorphic graphs
Two graphs which contain the same number of graph vertices connected in the same way are said to be isomorphic.
### Disjoint Paths
Two paths are said edge disjoint if they don’t share any edge.
### Connected graph
There is a path from any point to any other point in the graph.
### Acyclic graph
A graph having no graph cycles
### Hamiltonian Path
A graph path between two vertices of a graph that visits each vertex exactly once.
### Hamiltonian cycle
A Hamiltonian path whose endpoints are adjacent.
### Tree
An undirected graph in which any two vertices are connected by exactly one path
### Forest
An undirected graph in which any two vertices are connected by at most one path
### Spanning tree
Subset of graph G, which has all the vertices covered with minimum possible number of edges. Hence, a spanning tree does not have cycles and it cannot be disconnected.. A disconnected graph does not have any spanning tree, as it cannot be spanned to all its vertices.
### Spanning forest
In graphs that are not connected, there can be no spanning tree, and one must consider spanning forests instead
### Complement of a graph
The complement or inverse of a graph G is a graph H on the same vertices such that two distinct vertices of H are adjacent if and only if they are not adjacent in G
### Complete Clique
A clique in a graph G is a complete subgraph of G
### Directed graph or digraph
A graph of vertices connected by directed edges
### Directed Edge
An  edge with orientation, represented by an arrow
### Directed Acyclic graph (DAG)
A directed graph with no directed cycles
### Weighted graph
A graph in which a number (weight) is assigned to each edge
### Bipartie graph
A simple graph G = (V, E) with vertex partition V = {V1, V2} is called a bipartite graph if every edge of E joins a vertex in V1 to a vertex in V2.
### Union of two graphs
The union of two graphs is the graph induced by the union of their sets of edges.
### Density of a graphs
The average vertex degree of 2E/V
### Dense graph
The average vertex degree proportional to V
### Sparse graph
The complement graph is dense
### Incidence matrix
Way to represent a graph.The incidence matrix of G is an n × m matrix B = (bik ), where each row corresponds to a vertex and each column corresponds to an edge such that if ek is an edge between i and j, then all elements of column k are 0 except bik = bjk = 1.

Algorithms

<table>
  <tr>
    <th>Algorithm name</th>
    <th>Description</th>
    <th>Type</th>
    <th>Complexity</th>
  </tr>
  <tr>
    <td>Breadth first search </td>
    <td>Traversal</td>
    <td>Directed or not</td>
    <td> O(V + E)</td>
  </tr>
  <tr>
    <td>Depth first search </td>
    <td>Traversal</td>
    <td>Directed or not</td>
    <td> O(V + E)</td>
  </tr>
  <tr>
    <td>Dijkstra</td>
    <td>Shortest path</td>
    <td>weighted</td>
    <td> O ( V + E * log V ) </td>
  </tr>
  <tr>
    <td>Disjoint set (union-find)</td>
    <td>Detects cycles</td>
    <td>Directed or not</td>
    <td> O(n lg* n)</td>
  </tr>
  <tr>
    <td>Prim</td>
    <td>Minimum Spanning Tree</td>
    <td>weighted</td>
    <td>O(ElogV)</td>
  </tr>
    <tr>
    <td>Kruskal</td>
    <td>Minimum Spanning Tree</td>
    <td>weighted</td>
    <td>O(ElogV)</td>
  </tr>
</table>