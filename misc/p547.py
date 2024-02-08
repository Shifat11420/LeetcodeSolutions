# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
# A province is a group of directly or indirectly connected cities and no other cities outside of the group.
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
# Return the total number of provinces.

# Example 1:
# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2

# Example 2:
# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
 
# # Time: O(n*n), Space: O(n*n)
# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         n = len(isConnected)
#         adj = {i:[] for i in range(n)}
#         for r in range(n):
#             for c in range(n):
#                 if isConnected[r][c]==1:
#                     adj[r].append(c)
#                     adj[c].append(r)

#         def dfs(i):
#             visit.add(i)
#             for j in adj[i]:
#                 if j not in visit:
#                     dfs(j)

#         visit = set()
#         provinceCount = 0
#         for i in adj:      
#             if i not in visit:
#                 dfs(i)
#                 provinceCount += 1
#         return provinceCount            
        

#  Time: O(n), Space: O(1)
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        def dfs(i):
            visit.add(i)
            for j in range(n):
                if j not in visit and isConnected[i][j]==1:
                    dfs(j)

        visit = set()
        provinceCount = 0
        for i in range(n):      
            if i not in visit:
                dfs(i)
                provinceCount += 1
        return provinceCount            
                