""""""
"""
Adjacency List = List of lists

Adnatages of using List of Lists
1. No. extra info stored
2. Optimized

Finding neighbours is 0(1) time complexity
Adjacency matrix takes O(n) time, where n is number of vertices. 

For sorting, MSB type of taks, Edge lists are used.
"""


"""
Applications of Graphs:
a. Maps (Shortest Path)
b. Social Network
c. Delivery Network (Shortest Cyclic Route)
d. Molecules
e. Routing Algorithm
f. Machine learning - Deep learning
g. Computer vision - Image segmentation
h. Graph DB - Nebula, Neo4j
"""

# creating graph
# Edge will have src, dest and weight


class Edge:
    def __init__(self, s, d, w):
        self.src = s
        self.dest = d
        self.wt = w


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = {i: [] for i in range(vertices)}  # Dictionary to store adjacency list

    def add_edge(self, src, dest, weight):
        edge = Edge(src, dest, weight)
        self.adj_list[src].append(edge)

    def display(self):
        for vertex in self.adj_list:
            print(f"Vertex {vertex}: ", end="")
            for edge in self.adj_list[vertex]:
                print(f" -> (Dest: {edge.dest}, Weight: {edge.wt})", end="")
            print()  # Newline for clarity

    def get_neighbors(self, vertex):
        """Returns a list of neighbors (destination, weight) for the given vertex."""
        if vertex not in self.adj_list:
            return []
        return [(edge.dest, edge.wt) for edge in self.adj_list[vertex]]


# Creating a Graph with 5 vertices (0 to 4)
g = Graph(5)

# Adding some edges
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(2, 4, 5)
g.add_edge(3, 4, 7)

# Display the graph structure
g.display()

# Get neighbors of vertex 0
print("\nNeighbors of vertex 0:", g.get_neighbors(0))
# Get neighbors of vertex 3
print("Neighbors of vertex 3:", g.get_neighbors(3))

