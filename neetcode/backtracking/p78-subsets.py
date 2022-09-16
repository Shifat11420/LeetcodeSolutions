# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]]
 

# DFS 
# Complexity : time O(n * 2^n)
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        res = []
        
        def dfs(i):                    # i = index
            if i >= len(nums):
                res.append(subset.copy())          # copy because we will change/add to it later
                return
        
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1)
            
            # decision NOT to include nums[i]
            subset.pop()
            dfs(i+1)
            
        dfs(0)
        return res      