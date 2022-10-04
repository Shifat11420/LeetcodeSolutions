# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.
# You may assume that you have an infinite number of each kind of coin.
# The answer is guaranteed to fit into a signed 32-bit integer.

# Example 1:
# Input: amount = 5, coins = [1,2,5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1

# Example 2:
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.

# Example 3:
# Input: amount = 10, coins = [10]
# Output: 1

# unbounded Knapsack
# bottom up DP


# caching/ memoization
# Complexity: time O(n * m), space O(m*n)  m = total number of coins, n= total amount
from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        
        def dfs(i, a):
            if i == len(coins):
                return 0
            if a == amount:
                return 1
            if a > amount:
                return 0
            cache[(i,a)] = dfs(i, a+coins[i]) +dfs(i+1, a)  # not skipping coin at i +skipping coin at i
            return cache[(i,a)]
        return dfs(0, 0)

        
# 2D dynamic programming
# Complexity: time O(n*m), space O(m*n)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0]*(len(coins)+1) for i in range(amount+1)]
        dp[0] = [1]*(len(coins)+1)
            
        for a in range(amount+1):
            for i in range(len(coins)-1, -1, -1):
                dp[a][i] = dp[a][i+1]  # skipping coin at i
                if a-coins[i]>=0:
                    dp[a][i] += dp[a-coins[i]][i]    # not skipping coin at i
        return dp[amount][0]            

            
            
 # Complexity: time O(m*n), space O(n), 1 dimension of memory
# at any different time, we will only have two rows in memory
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]* (amount+1)
        dp[0] = 1
        
        for i in range(len(coins)-1, -1, -1):
            nextDP = [0]* (amount+1)
            nextDP[0] = 1
            for a in range(amount+1):
                nextDP[a] = dp[a]
                if a-coins[i]>=0:
                    nextDP[a] += nextDP[a-coins[i]]
            dp = nextDP        
        return dp[amount]     