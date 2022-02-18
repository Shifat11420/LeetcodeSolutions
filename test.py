#1. Two sum-------------------------------------------------------------------------

# using Two Pointer:
"""
#O(ngln), since we need to sort first
def twoSum(nums, target):
    left = 0
    right = len(nums)-1
       
    num_to_index = [(num, index) for index, num in enumerate(nums)]   
    num_to_index.sort()
   
    while left<right:
        if num_to_index[left][0]+num_to_index[right][0] == target:
            return [num_to_index[left][1], num_to_index[right][1]]
        elif num_to_index[left][0]+num_to_index[right][0] < target:
            left +=1
        else:
            right -=1
"""  

##using hash O(n)---best
"""
def twoSum(nums, target):
    mapping = {}
    
    for i in range(len(nums)):
        if target-nums[i] in mapping:
            return [i, mapping[target-nums[i]]]
        mapping[nums[i]] = i 
 
      
# nums = [-10,-1,-18,-19]
# target = -19
nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))
"""
# 11. Container With Most Water-------------------------------------------------------------------

# two pointer array
###probably O(n) time complexity, O(1) space complexity
"""
def maxArea(height):
    left = 0
    right =len(height)-1
    maxarea = 0
    
    while left<right:
        area = (right-left)* min(height[left],height[right])
        maxarea = max(area, maxarea)
        
        if left<right:
            left +=1
        else:
            right -=1   
    return maxarea         
            
height = [1,8,6,2,5,4,8,3,7]            
print(maxArea(height))

"""


#p36. Valid sudoku
## using array and set O(n^2)
"""   
def isValidSudoku(board) :
    for i in range(9):
        row = []
        col = []
        block = []
        for j in range(9):
            c = board[i][j] #go columnwise
            if c != '.':
                col.append(c)
                
            r = board[j][i] #go rowwise
            if r != '.':
                row.append(r)
                
            b = board[(i//3)*3+j//3][(i%3)*3+j%3]  #go blockwise
            if b != '.':
                block.append(b)

        if len(row)!= len(set(row)) or len(col)!=len(set(col)) or len(block)!= len(set(block)):
            return False
    return True
board =[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board))
"""