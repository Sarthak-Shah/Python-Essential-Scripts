""""""
from collections import defaultdict
from typing import List

"""
1466. Reorder Routes to Make All Paths Lead to the City Zero
There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities. 
Roads are represented by connections where connections[i] = [x, y] represents a road from city x to city y. 
The edges are directed. You need to swap the direction of some edges so that every city can reach city 0. 
Return the minimum number of swaps needed.


To summarize: we treat the graph as undirected just so that we can do a DFS starting at 0. 
During this DFS, every traversal we do is away from 0, so when we see an edge that we are crossing (node, neighbor) is 
in connections, we know we need to swap it (increment the answer).
"""


def minReorder(connections: List[List[int]]) -> int:
    roads = set()
    graph = defaultdict(list)
    for x, y in connections:
        graph[x].append(y)
        graph[y].append(x)
        roads.add((x, y))

    def dfs(node):
        ans = 0
        for neighbor in graph[node]:
            if neighbor not in seen:
                if (node, neighbor) in roads:
                    ans += 1
                seen.add(neighbor)
                ans += dfs(neighbor)

        return ans

    seen = {0}
    return dfs(0)


connections = [[0,1], [1,3], [2,3], [4,0], [4,5]]
print(minReorder(connections))
