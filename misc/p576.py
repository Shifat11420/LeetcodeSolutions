# There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.
# Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.

# Example 1:
# Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
# Output: 6

# Example 2:
# Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
# Output: 12

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9+7
        cache = {}

        def dfs(r,c, move):
            if (r,c,move) in cache:
                return cache[(r,c,move)]
            if (r<0 or r==m or c<0 or c==n):
                return 1
            if move==maxMove:
                return 0    
            res = 0
            res += dfs(r-1,c, move+1)% MOD
            res += dfs(r+1,c, move+1)% MOD
            res += dfs(r,c-1, move+1)% MOD
            res += dfs(r,c+1, move+1)% MOD
            cache[(r,c,move)] = res
            return res

        return dfs(startRow, startColumn, 0) % MOD