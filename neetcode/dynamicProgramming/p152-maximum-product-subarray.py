# Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.
# The test cases are generated so that the answer will fit in a 32-bit integer.
# A subarray is a contiguous subsequence of the array.

# Example 1:
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Example 2:
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

# Idea: keep track of max and min both to have all the info in the subarray. e.g. [-1,-2,-3] for (-1*-2) * -3 = -6 but max is -2*-3 = 6 and we dont want to miss that 
# For zero, reset max and min to 1
# Complexity: time O(n), space O(1)

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)  # base case for single element list
        curMax, curMin = 1, 1
        
        for n in nums:
            if n == 0:
                curMax , curMin = 1, 1
                continue
            tmp = n * curMax
            curMax = max(n * curMax, n* curMin, n)
            curMin = min(tmp , n* curMin, n)
            res = max(res, curMax)
        return res  
            
        