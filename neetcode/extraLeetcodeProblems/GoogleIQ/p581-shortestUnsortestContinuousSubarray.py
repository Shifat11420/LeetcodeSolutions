# Given an integer array nums, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.
# Return the shortest such subarray and output its length.

# Example 1:
# Input: nums = [2,6,4,8,10,9,15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: 0

# Example 3:
# Input: nums = [1]
# Output: 0

# Time : O(n), Space: O(1)
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        bigV, smallV = nums[0], nums[-1]
        right_i, left_i = -1, -1
        for i in range(1, len(nums)):
            if nums[i] >= bigV:
                bigV = nums[i]
            else:
                right_i = i

        for i in range(len(nums)-2, -1, -1):
            if nums[i] <= smallV:
                smallV = nums[i]
            else:
                left_i = i

        return 0 if right_i == left_i else right_i-left_i+1
