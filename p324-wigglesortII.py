# https://leetcode.com/problems/wiggle-sort-ii/
# Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

# You may assume the input array always has a valid answer.



from numpy import sort


nums = [1,3,2,2,3,1]




def wiggleSort(nums):
    nums.sort()
    print(nums)
    half = len(nums[::2])
    print(half)
    print(nums[:half][::-1], nums[half:][::-1])
    nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
    print(nums)
wiggleSort(nums)