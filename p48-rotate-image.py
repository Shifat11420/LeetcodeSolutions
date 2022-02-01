# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
#You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
        

def rotate(matrix):
    length = len(matrix)

    # for k in range(len(matrix)-2):
    #     for i in range(len(matrix)-1-2*k):
    #         temp = matrix[k][i+k]
    #         #print("temp = ", temp)
    #         matrix[k][i+k] =  matrix[length-(i+1+k)][k]
    #         matrix[length-(i+1+k)][k] = matrix[length-(1+k)][length-(i+1+k)]
    #         matrix[length-(1+k)][length-(i+1+k)] = matrix[i+k][length-(1+k)]
    #         matrix[i+k][length-(1+k)] = temp

    # for loop ans does not work for 2D matrices

    k = 0
    while (len(matrix)-2)>= k :
        for i in range(len(matrix)-1-2*k):
            temp = matrix[k][i+k]
            #print("temp = ", temp)
            matrix[k][i+k] =  matrix[length-(i+1+k)][k]
            matrix[length-(i+1+k)][k] = matrix[length-(1+k)][length-(i+1+k)]
            matrix[length-(1+k)][length-(i+1+k)] = matrix[i+k][length-(1+k)]
            matrix[i+k][length-(1+k)] = temp
        k += 1          


#matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
matrix = [[1,2,3],[4,5,6],[7,8,9]]
#matrix = [[1,2],[3,4]]
rotate(matrix)
print(matrix)