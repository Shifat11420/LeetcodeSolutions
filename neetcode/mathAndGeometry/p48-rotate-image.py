# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

# Example 2:
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 
# Complexity: time O(n*n), space O(1)
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r =0, len(matrix)-1
        
        while l<r:
            for i in range(r-l):
                top, bottom = l, r    #think about numbers they represent

                # save the top-left
                topLeft = matrix[top][l+i]   #i go right

                # move bottom-left to top-left
                matrix[top][l+i] = matrix[bottom-i][l]  # i go up

                # move bottom-right to bottom-left
                matrix[bottom-i][l] = matrix[bottom][r-i]  # i go left

                # move top-right to bottom-right
                matrix[bottom][r-i] = matrix[top+i][r]    # i go down

                # move top-left to top-right
                matrix[top+i][r] = topLeft

            # next step, iterate inside loops
            l += 1    
            r -= 1 