# Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.
# Return the maximum product you can get.

# Example 1:
# Input: n = 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.

# Example 2:
# Input: n = 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
 
# Time: O(n^2),  n subproblems and solve each is O(n) operations performed once
# Space : O(n), recursive call stack or cache
 
class Solution:
    # caching/memoization
    def integerBreak(self, n: int) -> int:
        dp = {1:1}

        def dfs(num):
            if num in dp:
                return dp[num]
            dp[num] = 0 if num==n else num  # makes sure, the original problem (say, n=4) has to be broken down but not the subproblems (1,3 or 2,2, not for 3 or 2 because 3 (prod 3)->1,2(prod 2) or 1,1,1(prod 1))

            for i in range(1,num):
                val = dfs(i)*dfs(num-i)
                dp[num] = max(dp[num], val)
            return dp[num]

        return dfs(n)        

    # DP 
    def integerBreak(self, n: int) -> int:
        dp = {1:1}    
       
        for num in range(2,n+1):
            dp[num] = 0 if num==n else num
            for i in range(1, num):
                val = dp[i]*dp[num-i]
                dp[num] = max(dp[num], val)
        return dp[n]        
