# Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

# Example 1:
# Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
# Output: true

# Example 2:
# Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
# Output: false

# valid tree- connected, no cycle/loop
# DFS, hashmap
# start at 0, check for every single node and their neighbors if they are connected
# maintain prev values to avoid false loop

# Complexity: time O(e+v), space O(e+v), e = number of edges, v = number of vertices 
def validTree(self, n, edges):
    if not n:
        return False               # empty tree is a valid tree

    adj = {i : [] for i in range(n)}       # node: [neighbors]
    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)    

    visit = set()
    def dfs(i, prev):
        if i in visit:
            return False                 # loop detection

        visit.add(i)

        for j in adj[i]:
            if j == prev:
                continue
            if not dfs(j,i):
                return False             # loop detection
        return True

    return dfs(0, -1) and n==len(visit)            