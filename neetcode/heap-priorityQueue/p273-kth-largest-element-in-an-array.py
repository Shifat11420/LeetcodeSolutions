# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# You must solve it in O(n) time complexity.

# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4


# Quick select algorithm, similar to quick sort, make array in halves, left part <= pivot < right part
# change position into places, no extra memory

# Complexity: O(n) -average case... worst case is O(n^2)
# how can we make sure this is always going to be half, turns out we can, so worst case is n^2 and average case n.

# for normal quick sort, it;s O(nlogn)
# average case --- at best look at one half of the array,  n + n/2 +n/4 .... = O(2n) = O(n)
# worst case ---if the pivot is the greatest element, so you eleminate one element at a time, so complexity n^2


# l, r left and right pointers
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) -k

        def quickselect(l, r):        # r is not inclusive
            pivot, p = nums[r], l     # pivot is the rightmost value, pointer p starts from the left
            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[p], nums[i] =nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]              # change pivot position 

            if p > k:   return quickselect(l, p-1)           # run on left half
            elif p < k: return quickselect(p+1, r)           # run on right half
            else:       return nums[p] 

        return quickselect(0, len(nums)-1)

nums = [3,2,3,1,2,4,5,5,6] 
k = 4
new = Solution
print(new().findKthLargest(nums, k))        