Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example 1:
Input: matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], [
    "1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
Output: 4

Example 2:
Input: matrix = [["0", "1"], ["1", "0"]]
Output: 1

Example 3:
Input: matrix = [["0"]]
Output: 0

# Time : O(m*n)
# Space : O(m*n)


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROW, COL = len(matrix), len(matrix[0])
        dp = [[0]*COL for _ in range(ROW)]

        maxsize = 0
        for r in range(ROW):
            for c in range(COL):
                if matrix[r][c] == "1":
                    if r == 0 or c == 0:
                        dp[r][c] = 1
                    else:
                        dp[r][c] = min(dp[r-1][c], dp[r-1][c-1], dp[r][c-1])+1
                    maxsize = max(maxsize, dp[r][c])

        return maxsize*maxsize
