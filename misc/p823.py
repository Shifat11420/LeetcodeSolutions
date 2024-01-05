# Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.
# We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.
# Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.

# Example 1:
# Input: arr = [2,4]
# Output: 3
# Explanation: We can make these trees: [2], [4], [4, 2, 2]

# Example 2:
# Input: arr = [2,4,5,10]
# Output: 7
# Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].

# Time: O(n^2+nlogn)~ O(n^2), Space : O(n) 
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = (10**9+7)
        arr.sort()
        dp = {}
        for ind,a in enumerate(arr):
            dp[a] = 1
            for j in range(ind):
                if a%arr[j]==0: 
                    factor = a//arr[j]
                    if factor in arr:
                        dp[a] = (dp[a] + dp[arr[j]]*dp[factor]) % MOD
        res = 0
        for val in dp.values():
            res  = (res+val) % MOD    
        return res            
