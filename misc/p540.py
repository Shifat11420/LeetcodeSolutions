# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
# Return the single element that appears only once.
# Your solution must run in O(log n) time and O(1) space.

# Example 1:
# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2

# Example 2:
# Input: nums = [3,3,7,7,10,11,11]
# Output: 10
 

# # Time: O(logn), Space: O(n)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        l, r = 0, len(nums)-1
        while l<=r:
            if r-l<=1:
                if nums[l]==nums[l-1]:
                    return nums[r]
                else:
                    return nums[l]    
            m = (l+r)//2
            res = nums[m+1:] if nums[m-1]== nums[m] else nums[m:]
            total = 0
            for n in res:
                total = total^n
            if total>0:
                l = m
            else:
                r = m
              
        

# Time: O(logn), Space: O(1)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        l, r = 0, len(nums)-1
        while l<=r:
            if r-l<=1:
                if nums[l]==nums[l-1]:
                    return nums[r]
                else:
                    return nums[l]    
            m = (l+r)//2
            x = m+1 if nums[m-1]== nums[m] else m
            res = r-x+1
            odd = res%2
            if odd:
                l = x
            else:
                r = m-2 if nums[m-1]== nums[m] else m-1       