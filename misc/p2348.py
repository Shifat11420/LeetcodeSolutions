# Given an integer array nums, return the number of subarrays filled with 0.
# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:
# Input: nums = [1,3,0,0,2,0,0,4]
# Output: 6
# Explanation: 
# There are 4 occurrences of [0] as a subarray.
# There are 2 occurrences of [0,0] as a subarray.
# There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.

# Example 2:
# Input: nums = [0,0,0,2,0,0]
# Output: 9
# Explanation:
# There are 5 occurrences of [0] as a subarray.
# There are 3 occurrences of [0,0] as a subarray.
# There is 1 occurrence of [0,0,0] as a subarray.
# There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9.

# Example 3:
# Input: nums = [2,10,2019]
# Output: 0
# Explanation: There is no subarray filled with 0. Therefore, we return 0.

class Solution:
    def countsubarray(self, length):
        # count = 0
        # for window in range(1,length+1):
        #     for i in range(length-window+1):
        #         count += 1
        # return count
        return (length * (length + 1)) // 2

    def zeroFilledSubarray(self, nums: List[int]) -> int:
        l, r = 0,0
        res = 0
        n= len(nums)

        while r< n:
            if nums[r]==0:
                l=r
                while r<n and nums[r]==0:
                    r+=1            
                length = r-l
                res += self.countsubarray(length)
            else:
                r+=1    
        return res