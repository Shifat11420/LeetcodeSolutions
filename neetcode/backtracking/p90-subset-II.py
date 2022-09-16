# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]]


# idea: difference with subset-I problem --> if a value occurs multiple times, when we choose to skip a duplicate, we should skip all the duplicates, just add once (do it after sorting)
# Complexity: time O(n*2^n+nlog) ~ O(n*2^n) ---worst case, nlogn for sorting
# each value 2 choices, n values in the input --> 2^n choices of subsets, how long each subset> at most n, so O(length of the subset * number of subsets)=O(n*2^n)

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()      #you want to sort it because it helps skipping the duplicates
        
        def backtrack(i, subset):   # i = index, subset = current subset
            # base case
            if i == len(nums):
                res.append(subset[::])      #copy of subset
                return

            # decision to include nums[i]
            subset.append(nums[i])
            backtrack(i+1, subset)

            #decision NOT to include nums[i]
            subset.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i += 1
            backtrack(i+1, subset)
        
        backtrack(0, [])
        return res     