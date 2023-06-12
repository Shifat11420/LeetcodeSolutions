# Given an integer array nums sorted in non-decreasing order and an integer target, return true if target is a majority element, or false otherwise.
# A majority element in an array nums is an element that appears more than nums.length / 2 times in the array.

# Example 1:
# Input: nums = [2,4,5,5,5,5,5,6,6], target = 5
# Output: true
# Explanation: The value 5 appears 5 times and the length of the array is 9.
# Thus, 5 is a majority element because 5 > 9/2 is true.

# Example 2:
# Input: nums = [10,100,101,101], target = 101
# Output: false
# Explanation: The value 101 appears 2 times and the length of the array is 4.
# Thus, 101 is not a majority element because 2 > 4/2 is false.


class Solution:
    # O(n) time, O(1)
    # def isMajorityElement(self, nums: List[int], target: int) -> bool:
    #     count = 0
    #     for n in nums:
    #         if n == target:
    #             count += 1
    #     if count>len(nums)/2:
    #         return True
    #     return False

    # time O(logn), space O(1)
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        def search(arr, x):
            lo, hi = 0, len(arr)
            while lo < hi:
                m = (lo+hi)//2
                if arr[m] < x:
                    lo = m+1
                else:
                    hi = m
            return lo

        if nums[len(nums)//2] != target:
            return False

        lo = search(nums, target)
        hi = search(nums, target+1)
        return (hi-lo) > len(nums)//2
