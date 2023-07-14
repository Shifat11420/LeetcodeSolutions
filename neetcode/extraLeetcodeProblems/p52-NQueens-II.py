# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
# Given an integer n, return the number of distinct solutions to the n-queens puzzle.

# Example 1:
# Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

# Example 2:
# Input: n = 1
# Output: 1

class Solution:
    def totalNQueens(self, n: int) -> int:
        posDiag = set()
        negDiag = set()
        col = set()

        res = set()
        board = [["."]*n for i in range(n)]

        def backtrack(r):
            if r == n:
                # add a valid solution
                res.add(map('#'.join, map(''.join, board)))
                return

            count = 0
            for c in range(n):
                if c in col or r+c in posDiag or r-c in negDiag:
                    continue
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)

                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."

        backtrack(0)
        return len(res)

# Optimized solution:
# If you observe the exploration path that solution tree takes, you would notice that it starts at a different row each time. Each path it takes is unique. So instead of tracking the valid solutions. We can just track the count of valid solutions. Whenever we hit the required number of queens, we just add that path to overall tally.

# Time - O(N!) - In the solution tree, number of valid exploration paths from a node reduces by 2 at each level. In first level, we have N columns options to place the queen i.e N paths from the root node. In the next level, we have max N-2 options available because we can't place the queen in same column and same diagonal as previous queen. In the next level, it will be N-4 because of two columns and two diagonals occupied by previous two queens. This will continue and give us a O(N!)Time.
# Space - O(N^2) - recursive call stack to explore all possible solutions


class Solution:
    def totalNQueens(self, n: int) -> int:
        posDiag = set()
        negDiag = set()
        col = set()

        def backtrack(r):
            if r == n:
                return 1
            count = 0
            for c in range(n):
                if c in col or r+c in posDiag or r-c in negDiag:
                    continue
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)

                count += backtrack(r+1)

                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
            return count
        return backtrack(0)
