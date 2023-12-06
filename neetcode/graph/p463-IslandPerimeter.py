# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

# Example 1:
# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.

# Example 2:
# Input: grid = [[1]]
# Output: 4

# Example 3:
# Input: grid = [[1,0]]
# Output: 4

# Time: O(mn), Space: O(mn)
# Linear function, linear complexity, only visit each cell once and size of grid is mn
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visit = set()

        def dfs(r,c,visit, count):
            if (r<0 or r==ROW or c<0 or c==COL or grid[r][c]==0):
                return 1
            if (r,c) in visit:
                return 0 
                           
            visit.add((r,c))
            count = 0
            count += dfs(r+1,c, visit, count)
            count += dfs(r-1,c, visit, count)
            count += dfs(r,c+1, visit, count)
            count += dfs(r,c-1, visit, count)
            return count

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]==1:
                    return dfs(r,c,visit,count)

             