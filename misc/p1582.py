# Given an m x n binary matrix mat, return the number of special positions in mat.
# A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

# Example 1:
# Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
# Output: 1
# Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.

# Example 2:
# Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
# Explanation: (0, 0), (1, 1) and (2, 2) are special positions.

# Time : O(mn), Space : O(mn)
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row = collections.defaultdict(int)
        col = collections.defaultdict(int)

        for i in range(m):
            for j in range(n):
                if mat[i][j]== 0:
                    continue
                row[i] += 1
                col[j] += 1

        res = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j]== 0:
                    continue
                if row[i]==1 and col[j]==1:
                    res += 1
        return res                            