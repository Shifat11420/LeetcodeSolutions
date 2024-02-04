# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
# The distance between two adjacent cells is 1.

# Example 1:
# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]

# Example 2:
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]
 
# Time: O(m*n), Space: O(m*n)
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        q = deque()
        for r in range(m):
            for c in range(n):
                if mat[r][c]==0:
                    q.append((r,c))
                else:
                    mat[r][c] = m*n

        directions = [[-1,0], [1,0], [0,1], [0,-1]]
        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                r, c = row+dr, col+dc
                if 0<=r<m and 0<=c<n:
                    if mat[r][c]>1+mat[row][col]:
                        mat[r][c] = 1+mat[row][col]
                        q.append((r,c))
        return mat                

