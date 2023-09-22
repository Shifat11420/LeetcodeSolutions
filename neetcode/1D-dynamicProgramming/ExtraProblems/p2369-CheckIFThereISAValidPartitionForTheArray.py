# You are given a 0-indexed integer array nums. You have to partition the array into one or more contiguous subarrays.
# We call a partition of the array valid if each of the obtained subarrays satisfies one of the following conditions:
# The subarray consists of exactly 2, equal elements. For example, the subarray [2,2] is good.
# The subarray consists of exactly 3, equal elements. For example, the subarray [4,4,4] is good.
# The subarray consists of exactly 3 consecutive increasing elements, that is, the difference between adjacent elements is 1. For example, the subarray [3,4,5] is good, but the subarray [1,3,5] is not.
# Return true if the array has at least one valid partition. Otherwise, return false.

# Example 1:
# Input: nums = [4,4,4,5,6]
# Output: true
# Explanation: The array can be partitioned into the subarrays [4,4] and [4,5,6].
# This partition is valid, so we return true.

# Example 2:
# Input: nums = [1,1,1,2]
# Output: false
# Explanation: There is no valid partition for this array.

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        def isvalid(arr):
            if len(arr)==2:
                if arr[0]==arr[1]:
                    return True
            if len(arr)==3:
                if arr[0]==arr[1]==arr[2] or arr[2]==arr[1]+1==arr[0]+2:
                    return True
            return False  

        # Memoization
        # Time: O(n), Space O(n)
        dp = {}
        def dfs(i):
            if i==len(nums):
                return True
            if i in dp:
                return dp[i]
            res = False        
            if i+1<=len(nums) and isvalid(nums[i:i+2]):
                res = dfs(i+2)
            if i+2<=len(nums) and isvalid(nums[i:i+3]):
                res = res or dfs(i+3)   
            dp[i]= res  
            return dp[i]

        return dfs(0)    

        # Time: O(n), Space O(1)
        # dp
        two = isvalid(nums[-2:])
        if len(nums)==2:
            return two
        three = isvalid(nums[-3:])

        dp = [three, two, False]

        for i in range(len(nums)-4, -1, -1):
            cur = isvalid(nums[i:i+2]) and dp[1]
            cur = cur or (isvalid(nums[i:i+3]) and dp[2])
            dp = [cur, dp[0], dp[1]]
        return dp[0]              