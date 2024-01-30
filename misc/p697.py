# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

# Example 1:
# Input: nums = [1,2,2,3,1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.

# Example 2:
# Input: nums = [1,2,2,3,1,4,2]
# Output: 6
# Explanation: 
# The degree is 3 because the element 2 is repeated 3 times.
# So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
 
# Time : O(n), Space : O(n)
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = Counter(nums)
        maxE = []
        maxV = max(count.values())
        if maxV==1:
            return 1

        for k, v in count.items():
            if v==maxV:
                maxE.append(k)

        minlen = float(inf)
        for i in maxE:
            l, r = 0, len(nums)-1
            while l<r and nums[l]!=i:
                l += 1
            while l<r and nums[r]!=i:
                r -= 1  
            minlen = min(minlen, r-l+1)  
            # li = nums.index(i)
            # ri = len(nums)-nums[::-1].index(i)
            # minlen = min(minlen, ri-li)    
        return minlen    
