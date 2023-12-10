# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2

# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mapp = {0:1}
        total = 0
        res = 0

        for n in nums:
            total += n                            # sum(nums[i:j]) = k    
            if total - k in mapp:                 # sum(nums[:j])-sum[nums[:i]] = k
                res += mapp[total-k]              # total-k = sum(nums[:i])

            mapp[total] = 1 + mapp.get(total, 0)
        return res            
