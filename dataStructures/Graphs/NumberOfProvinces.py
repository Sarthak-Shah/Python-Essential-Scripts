"""
"""
"""
There are n cities. Some of them are connected, while some are not. 
If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
A province is a group of directly or indirectly connected cities and no other cities outside of the group.
You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, 
and isConnected[i][j] = 0 otherwise.
Return the total number of provinces.

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
"""

"""
We can see that this is an undirected graph where the graph is given as an adjacency matrix, and the problem is asking 
for the number of connected components. We can think of each city as a node and each connected component as a province.
"""

from collections import defaultdict


def countProvinces(isConnected: list[list[int]]):
    def dfs(node):
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                dfs(neighbor)

    n = len(isConnected)
    graph = defaultdict(list)
    for i in range(n):
        for j in range(i+1, n):
            if isConnected[i][j]:
                graph[i].append(j)
                graph[j].append(i)

    seen = set()
    ans = 0

    for i in range(n):
        if i not in seen:
            ans += 1
            seen.add(i)
            dfs(i)

    return ans

"""
Let's quickly talk about the code implementation and how implementing DFS here differs from trees. 
As mentioned before, with trees, we are given objects representing the nodes.
Here, the nodes aren't exactly given to us. We are simply told that there exists some nodes numbered from 0 to n - 1, 
and we are given information regarding the edges.

Here, we pass the integer label of the node. This is a concept that you will need to master - with graphs, 
the graph only "exists" as an idea. It is up to you to implement a method of representing the nodes and edges and traversing over them. 
Thankfully, most graph problems will have the nodes labeled [0, n - 1], so we can re-use a lot of the logic between problems.
"""

# Example usage:
isConnected = [[1,1,0], [1,1,0], [0,0,1]]
print(countProvinces(isConnected))  # Output: 2

