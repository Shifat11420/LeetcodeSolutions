#Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

# https://www.youtube.com/watch?v=8f1XPm4WOUc
# Union-find algorithm
# start with separate connected component for each node, as connect, decrease the number
# parent array and rank array- size of entire connected component, increase as connect
# if the root parent are same, they are connected



#Complexity: O(e+v) --check
from typing import List

class Solution:
    def countComponents(self, n:int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]         #parent array
        rank = [1] * n

        def find(n1):
            res = n1    
            while res != par[res]:
                par[res] = par[par[res]]    #path compression
                res = par[res]
            return res

        def union(n1,n2):
            p1, p2 = find(n1), find(n2)        
            if p1==p2:
                return 0
            if rank[p1]>rank[p2]:
                par[p2] =p1
                rank[p1] += rank[p2]
            else:
                par[p1] =p2
                rank[p2] += rank[p1]
            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)        
        return res

n= 5
edges = [[0,1], [1,2], [3,4]]
new = Solution
print(new().countComponents(n, edges))

        