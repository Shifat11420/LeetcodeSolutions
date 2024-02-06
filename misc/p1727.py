# You are given a binary matrix matrix of size m x n, and you are allowed to rearrange the columns of the matrix in any order.
# Return the area of the largest submatrix within matrix where every element of the submatrix is 1 after reordering the columns optimally.

# Example 1:
# Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
# Output: 4
# Explanation: You can rearrange the columns as shown above.
# The largest submatrix of 1s, in bold, has an area of 4.

# Example 2:
# Input: matrix = [[1,0,1,0,1]]
# Output: 3
# Explanation: You can rearrange the columns as shown above.
# The largest submatrix of 1s, in bold, has an area of 3.

# Example 3:
# Input: matrix = [[1,1,0],[1,0,1]]
# Output: 2
# Explanation: Notice that you must rearrange entire columns, and there is no way to make a submatrix of 1s larger than an area of 2.
 
# Time: O(row*col*log(col)), Space: O(collog(col)) for sorting
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        for r in range(1,row):
            for c in range(col):
                if matrix[r][c]==1:
                    matrix[r][c] += matrix[r-1][c]

        maxarea = 0
        for r in range(row):
            matrix[r].sort()
            for c in range(col):
                height = matrix[r][c]
                width = col-c
                area = height*width
                maxarea = max(maxarea, area)
        return maxarea