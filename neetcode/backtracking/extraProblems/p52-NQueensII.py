# Problem- 52  N-Queens II
# ------------------------
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
# Given an integer n, return the number of distinct solutions to the n-queens puzzle.

# Example 1:
# Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

# Example 2:
# Input: n = 1
# Output: 1
# ---------------------------------
class Solution:
    def totalNQueens(self, n: int) -> int:
        posDiag = set()
        negDiag = set()
        col = set()

        def backtrack(r):
            if r==n:
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