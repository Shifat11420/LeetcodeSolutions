# You are given a 0-indexed 2D integer matrix grid of size 3 * 3, representing the number of stones in each cell. The grid contains exactly 9 stones, and there can be multiple stones in a single cell.
# In one move, you can move a single stone from its current cell to any other cell if the two cells share a side.
# Return the minimum number of moves required to place one stone in each cell.

# Example 1:
# Input: grid = [[1,1,0],[1,1,1],[1,2,1]]
# Output: 3
# Explanation: One possible sequence of moves to place one stone in each cell is: 
# 1- Move one stone from cell (2,1) to cell (2,2).
# 2- Move one stone from cell (2,2) to cell (1,2).
# 3- Move one stone from cell (1,2) to cell (0,2).
# In total, it takes 3 moves to place one stone in each cell of the grid.
# It can be shown that 3 is the minimum number of moves required to place one stone in each cell.

# Example 2:
# Input: grid = [[1,3,0],[1,0,0],[1,0,3]]
# Output: 4
# Explanation: One possible sequence of moves to place one stone in each cell is:
# 1- Move one stone from cell (0,1) to cell (0,2).
# 2- Move one stone from cell (0,1) to cell (1,1).
# 3- Move one stone from cell (2,2) to cell (1,2).
# 4- Move one stone from cell (2,2) to cell (2,1).
# In total, it takes 4 moves to place one stone in each cell of the grid.
# It can be shown that 4 is the minimum number of moves required to place one stone in each cell.
 
# Constraints:
# grid.length == grid[i].length == 3
# 0 <= grid[i][j] <= 9
# Sum of grid is equal to 9.

# Permutatio
# Time: O(9!), Space: O(9)
class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        zeroes = []
        sources = []
        for r in range(3):
            for c in range(3):
                if grid[r][c]==0:
                    zeroes.append([r,c])
                elif grid[r][c]>1:
                    t = grid[r][c]-1
                    while t>0:
                        sources.append([r,c])
                        t -= 1    

        def distance(p1,p2):
            return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
            
        p = itertools.permutations(sources, len(zeroes))
        minsteps = float(inf)    
        for perm in p:
            moves = 0    
            for i in range(len(zeroes)):
                moves += distance(perm[i],zeroes[i])
            minsteps = min(minsteps, moves)    
        return minsteps    


# DFS+ Backtracking -most efficient
# Time: O(9!), Space: O(9)
class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        zeroes = []
        sources = []
        for r in range(3):
            for c in range(3):
                if grid[r][c]==0:
                    zeroes.append([r,c])
                elif grid[r][c]>1:
                    sources.append([r,c])
   

        def distance(p1,p2):
            return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
                 
        def dfs(i):
            if i==len(zeroes):
                return 0
            minsteps = float(inf)
            for s in sources:
                moves = 0
                r, c = s
                if grid[r][c]<=1:
                    continue
                grid[r][c] -= 1
                moves = distance(s, zeroes[i]) + dfs(i+1)             
                minsteps = min(minsteps, moves)
                grid[r][c] += 1
            return minsteps  
        
        return dfs(0)