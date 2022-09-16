# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

# Example 3:
# Input: nums = [1]
# Output: [[1]]

# choices top down the tree: pop first element
# choices bottom up the tree:  add the element at the end

# Complexity: 
    # Time: between O(n!) and O(n * n!)
    # Space: O(n * n!) it's the space taken by res
# Comment: If using mutable collection, time complexity is exactly the space complexity for output: O(n * n!).
# The list instance is created "only" at the base case. Then the result of base case is always reused and mutated with O(1) time complexity to add single value.
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        if len(nums)==1:
            return [nums[:]]     #copy of nums
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)       #recursion
            
            #bottom up
            for perm in perms:
                perm.append(n)
            result.extend(perms)          # add the permutation
            nums.append(n)              # add to the end
            
        return result   