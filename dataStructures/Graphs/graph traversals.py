
""
"""
Type of Traversals:

1) Breadth first serach:
- Go to immediate neighbours first
- Level wise traverse - kind of level order traversal of Binary Tree
- Cycle exist in Graph, so extra visitor array required to track visited Nodes otherwise repeatation occurs.


2) Depth first search


"""
from collections import deque

from collections import deque


def bfs_using_queue(graph, start_node):
    visited = set()  # To keep track of visited nodes
    queue = deque([start_node])  # Queue for BFS

    while queue:
        node = queue.popleft()  # Dequeue from the front (FIFO)
        if node not in visited:
            print(node, end=" ")  # Processing the node
            visited.add(node)

            # Add all unvisited neighbors to the queue
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)


# Example graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Run BFS starting from 'A'
bfs_using_queue(graph, 'A')
