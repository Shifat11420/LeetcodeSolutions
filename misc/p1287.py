# Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

# Example 1:
# Input: arr = [1,2,2,6,6,6,6,7,10]
# Output: 6

# Example 2:
# Input: arr = [1,1]
# Output: 1

# Time : O(n), Space : O(1)
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        length = len(arr)
        targetlen = length/4

        l, r = 0, 1
        while r<length:
            while r<length and arr[l]==arr[r]:
                r+=1
            if r-l>targetlen:
                return arr[l]
            l = r
            r = r+1        
        return arr[l]    