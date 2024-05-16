# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Example 2:
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
 
# Constraints:
# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105

# Time: O(n), Space: O(1)
# Notes: If you don't use any sort of subscription ([:]) the variable won't be modified in-place, but, instead, it would point to another place in the memory, receiving a different id
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(arr):
            l, r = 0, len(arr)-1
            while l<=r:
                arr[l], arr[r] = arr[r], arr[l]
                l+=1
                r-=1
            return arr
        
        if k==0:
            return nums
        n = len(nums)
        k = k%n
        nums[:] = reverse(nums)
        nums[:] = reverse(nums[:k]) + reverse(nums[k:])   
        return nums
