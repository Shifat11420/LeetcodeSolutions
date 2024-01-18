# You are given an n x n binary matrix grid where 1 represents land and 0 represents water.
# An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.
# You may change 0's to 1's to connect the two islands to form one island.
# Return the smallest number of 0's you must flip to connect the two islands.

# Example 1:
# Input: grid = [[0,1],[1,0]]
# Output: 1

# Example 2:
# Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
# Output: 2

# Example 3:
# Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Output: 1


# Time: O(mn), Space: O(mn)
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        def dfs(r,c, visit):
            if (r<0 or r==ROW or c<0 or c==COL or (r,c) in visit or grid[r][c]!=1):
                return
            visit.add((r,c))
            dfs(r+1,c, visit)
            dfs(r-1,c, visit)
            dfs(r,c+1, visit)
            dfs(r,c-1, visit)
            return visit

        # visitone = set()
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]==1:
                    visitone = dfs(r,c, set())
                    break
        q = deque(visitone) 

        directions = [[-1,0], [1,0], [0,1], [0,-1]]
        step = 0
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if (r<0 or r==ROW or c<0 or c==COL or (r,c) in visitone):
                        continue
                    if grid[r][c]==1:
                        return step
                    q.append((r,c)) 
                    visitone.add((r,c))   
            step += 1
        return -1    

        