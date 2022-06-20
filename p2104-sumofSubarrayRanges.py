# 2104. Sum of Subarray Ranges
# You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.
# Return the sum of all subarray ranges of nums.
# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:

# Input: nums = [1,2,3]
# Output: 4
# Explanation: The 6 subarrays of nums are the following:
# [1], range = largest - smallest = 1 - 1 = 0 
# [2], range = 2 - 2 = 0
# [3], range = 3 - 3 = 0
# [1,2], range = 2 - 1 = 1
# [2,3], range = 3 - 2 = 1
# [1,2,3], range = 3 - 1 = 2
# So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.
# Example 2:

# Input: nums = [1,3,3]
# Output: 4
# Explanation: The 6 subarrays of nums are the following:
# [1], range = largest - smallest = 1 - 1 = 0
# [3], range = 3 - 3 = 0
# [3], range = 3 - 3 = 0
# [1,3], range = 3 - 1 = 2
# [3,3], range = 3 - 3 = 0
# [1,3,3], range = 3 - 1 = 2
# So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.
# Example 3:

# Input: nums = [4,-2,-3,4,1]
# Output: 59
# Explanation: The sum of all subarray ranges of nums is 59.
#----------------------concept------------------------------------------

# What can monotonous increase stack do?
# (1) find the previous less element of each element in a vector with O(n) time:
# (2) find the next less element of each element in a vector with O(n) time:
# How can the monotonous increase stack be applied to this problem?
# For example:
# Consider the element 3 in the following vector:

#                             [2, 9, 7, 8, 3, 4, 6, 1]
# 			     |                    |
# 	             the previous less       the next less 
# 	                element of 3          element of 3

# After finding both NLE and PLE of 3, we can determine the
# distance between 3 and 2(previous less) , and the distance between 3 and 1(next less).
# In this example, the distance is 4 and 3 respectively.
# How many subarrays with 3 being its minimum value?
# The answer is 4*3.

# 9 7 8 3 
# 9 7 8 3 4 
# 9 7 8 3 4 6 
# 7 8 3 
# 7 8 3 4 
# 7 8 3 4 6 
# 8 3 
# 8 3 4 
# 8 3 4 6 
# 3 
# 3 4 
# 3 4 6
# How much the element 3 contributes to the final answer?
# It is 3*(4*3).
# The last thing that needs to be mentioned for handling duplicate elements:
# Method: Set strict less and non-strict less(less than or equal to) for finding NLE and PLE respectively. The order doesn't matter.

# class Solution:
#     def subArrayRanges(self, nums: List[int]) -> int:
def subArrayRanges(nums):    
    res = 0
    min_stack, max_stack = [], []
    n = len(nums)
    nums.append(0)

    for i, num in enumerate(nums):
        while min_stack and (i == n or num < nums[min_stack[-1]]):
            top = min_stack.pop()
            starts = top - min_stack[-1] if min_stack else top + 1
            ends = i - top
            res -= starts * ends * nums[top]
            
        min_stack.append(i)
        
        while max_stack and (i == n or num > nums[max_stack[-1]]):
            top = max_stack.pop()
            starts = top - max_stack[-1] if max_stack else top + 1
            ends = i - top
            res += starts * ends * nums[top]
            
        max_stack.append(i)
    
    return res


###-------------------- OUTPUT-------------- ###

# nums = [4,-2,-3,4,1]
# print(subArrayRanges(nums))

# nums :  [4, -2, -3, 4, 1, 0]
# -----------------------------------------------------------
# i, num --  0 4
# min_stack :  [0]
# max_stack :  [0]
# -----------------------------------------------------------
# i, num --  1 -2
# i , num,  nums[min_stack[-1]]--- 1 -2 4
# top =  0
# starts=  1 ends=  1
# starts * ends * nums[top]   4
# res=  -4
# min_stack :  [1]
# max_stack :  [0, 1]
# -----------------------------------------------------------
# i, num --  2 -3
# i , num,  nums[min_stack[-1]]--- 2 -3 -2
# top =  1
# starts=  2 ends=  1
# starts * ends * nums[top]   -4
# res=  0
# min_stack :  [2]
# max_stack :  [0, 1, 2]
# -----------------------------------------------------------
# i, num --  3 4
# min_stack :  [2, 3]
# i, num,  nums[max_stack[-1]]--- 3 4 -3
# top in max =  2
# in max starts=  1 ends=  1
# starts * ends * nums[top]   -3
# res=  -3
# i, num,  nums[max_stack[-1]]--- 3 4 -2
# top in max =  1
# in max starts=  1 ends=  2
# starts * ends * nums[top]   -4
# res=  -7
# max_stack :  [0, 3]
# -----------------------------------------------------------
# i, num --  4 1
# i , num,  nums[min_stack[-1]]--- 4 1 4
# top =  3
# starts=  1 ends=  1
# starts * ends * nums[top]   4
# res=  -11
# min_stack :  [2, 4]
# max_stack :  [0, 3, 4]
# -----------------------------------------------------------
# i, num --  5 0
# i , num,  nums[min_stack[-1]]--- 5 0 1
# top =  4
# starts=  2 ends=  1
# starts * ends * nums[top]   2
# res=  -13
# i , num,  nums[min_stack[-1]]--- 5 0 -3
# top =  2
# starts=  3 ends=  3
# starts * ends * nums[top]   -27
# res=  14
# min_stack :  [5]
# i, num,  nums[max_stack[-1]]--- 5 0 1
# top in max =  4
# in max starts=  1 ends=  1
# starts * ends * nums[top]   1
# res=  15
# i, num,  nums[max_stack[-1]]--- 5 0 4
# top in max =  3
# in max starts=  3 ends=  2
# starts * ends * nums[top]   24
# res=  39
# i, num,  nums[max_stack[-1]]--- 5 0 4
# top in max =  0
# in max starts=  1 ends=  5
# starts * ends * nums[top]   20
# res=  59
# max_stack :  [5]
# 59