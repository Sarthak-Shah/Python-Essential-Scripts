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


"""
200. Number of Islands

Given an m x n 2D binary grid which represents a map of 1 (land) and 0 (water), return the number of islands. 
An island is surrounded by water and is formed by connecting adjacent land cells horizontally or vertically.

As mentioned earlier, a graph can be given in the form of a matrix where squares are nodes and their neighbors are the 
adjacent squares. In this problem, it says that land is connected horizontally (left/right) or vertically (up/down). 
We can think of each land square as a node, and the up/down/left/right relationship forming edges. 
The problem is asking us for the number of islands, aka the number of connected components.

It seems this problem is very similar to the previous one. In fact, it is the exact same problem 
(find the number of connected components in an undirected graph), the format of the graph is just different. 
Let's use the same algorithm, but implemented according to this new format.
"""

def numIslands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    seen = set()  # To track visited land cells
    island_count = 0

    def dfs(r, c):
        if (r, c) in seen or r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
            return
        seen.add((r, c))  # Mark cell as visited

        # Explore all four directions
        dfs(r + 1, c)  # Down
        dfs(r - 1, c)  # Up
        dfs(r, c + 1)  # Right
        dfs(r, c - 1)  # Left

    # Scan the grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in seen:  # Found an unvisited island
                island_count += 1
                dfs(r, c)  # Explore the entire island

    return island_count
