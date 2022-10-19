# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1

# XOR of bit representation, 1^1 = 0, 0^0 = 0, 1^0 =1, 0^1 = 0
# Complexity: time O(n), space O(1)
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res  = 0  # n^0 = n
        for n in nums:
            res = n ^ res
        return res           # res would have that single number that does not match
        
        