# You are given an m x n grid where each cell can have one of three values:
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

# Example 1:
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4

# Example 2:
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

# Example 3:
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.


# multisource BFS--- DFS does not work because it's working from multiple source
# keep track of how many oranges are initially, 
# BFS - count fresh oranges, include all the rotten oranges to queue, pop in each unit of time and make adjancent fresh oranges rot, if queue empty and there is still fresh oranges, that's fresh, impossible.  

# Complexity: O(n*m), n,m dimensions of the grid
from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0
        
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])
                    
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        while q and fresh>0:
            for i in range(len(q)):   # multiple source, and a snap of q that be updated 
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r+dr, c+dc
                    # if in bounds and fresh, make rotten
                    if (row<0 or row==ROWS or col<0 or col==COLS or grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    q.append([row,col])        # update q with new rotten oranges
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1    