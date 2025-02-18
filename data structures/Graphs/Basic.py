##
""""""
"""
Graphs = Netowrk of nodes 
Parent of Tree structure

Here, Nodes = Vertices (Node -> Vertex)
Branch = Edge

Edges:
Two types:

1. uni-directional
    A ---> B
2. Un-directed / Bi-directional
    A ---- B
    A <---> B

Edge Weight = Value associated with the edge

1. Weighted graph
2. Un weighted  graph

So, depend on direction and weight we can have 4 types of graphs.
Ex, undirected weighted graph, unidirected un weighted graph etc..
"""

"""
Storing a Graph:
There are multiple ways to represent graphs in Python, depending on whether you need an adjacency matrix, 
an adjacency list, or a more feature-rich implementation using libraries like NetworkX.
"""
# 1. Using an Adjacency List (Dictionary of Lists) (Best for sparse graph)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Example: Print neighbors of 'A'
print(graph['A'])  # Output: ['B', 'C']

# 2. Using an Adjacency Matrix (2D List) (Best for dense graph)
# Adjacency Matrix for a graph with 4 nodes (0, 1, 2, 3)
graph = [
    [0, 1, 1, 0],  # Connections from node 0
    [1, 0, 1, 1],  # Connections from node 1
    [1, 1, 0, 1],  # Connections from node 2
    [0, 1, 1, 0]   # Connections from node 3
]

# Example: Check if node 0 is connected to node 2
print(graph[0][2])  # Output: 1 (Yes, there is an edge)

# 3. Using a Class-Based Approach
# This provides better scalability and structure.


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)  # For an undirected graph

    def display(self):
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")


# Example usage
g = Graph()
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.display()
