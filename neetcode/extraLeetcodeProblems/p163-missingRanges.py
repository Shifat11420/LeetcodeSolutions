# You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are within the inclusive range.
# A number x is considered missing if x is in the range [lower, upper] and x is not in nums.
# Return the shortest sorted list of ranges that exactly covers all the missing numbers. That is, no element of nums is included in any of the ranges, and each missing number is covered by one of the ranges.

# Example 1:
# Input: nums = [0,1,3,50,75], lower = 0, upper = 99
# Output: [[2,2],[4,49],[51,74],[76,99]]
# Explanation: The ranges are:
# [2,2]
# [4,49]
# [51,74]
# [76,99]

# Example 2:
# Input: nums = [-1], lower = -1, upper = -1
# Output: []
# Explanation: There are no missing ranges since there are no missing numbers.

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
       
        def helper(a,b):
            if a == b:
                return [a,a] 
            else:
                return [a,b] 

        nums = [lower-1] + nums + [upper+1] # that's the trick to avoid edge cases

        ans = [] 
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] > 1:
                ans.append(helper(nums[i-1]+1,nums[i]-1))
        return ans