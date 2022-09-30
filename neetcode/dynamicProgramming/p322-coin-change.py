# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.

# Example 1:
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# Example 2:
# Input: coins = [2], amount = 3
# Output: -1

# Example 3:
# Input: coins = [1], amount = 0
# Output: 0
 
# Complexity: time O(amount*no of coins), space O(amount), we will cache for every single value till amount
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)  # [maxvalue]* we will calculate  0 to amount
        dp[0] = 0   # base case
        
        for a in range(1, amount+1):  # go reverse 1,2,3..
            for c in coins:
                if (a-c)>=0:
                    dp[a] = min(dp[a], 1+dp[a-c])  # a=7, c=4 ,dp[7] = 1+dp[3]  # recursive relation
        return dp[amount] if dp[amount]!= (amount+1) else -1             