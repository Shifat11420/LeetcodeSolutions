# You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.
# If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.
# Return the maximum coins you can collect by bursting the balloons wisely.

# Example 1:
# Input: nums = [3,1,5,8]
# Output: 167
# Explanation:
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

# Example 2:
# Input: nums = [1,5]
# Output: 10

# Idea: what happens if we pop 3 last?
# [3,1,5,8]--> 1[3,1,5,8]1--? 1[3,_, _, _]1--> 1*3*1
# nums[L-1].3.nums[R+1] + DP[L+1][R]
# what happens if we pop 5 last?
# [3,1,5,8]--> 1[3,1,5,8]1--? 1[_,1,_, _]1--> 1*1*1
# nums[L-1].1.nums[R+1] + DP[i+1][R] + DP[L]{i-1}

# neetcode solution, time limit exceeded
# Complexity: time O(n^3) (n^2 is total subarrays and iterating through every single value->n), space O(n^2)
from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}
        
        
        def dfs(l,r):      # left and right boundaries of indices of the input array # O(n*n)
            if l>r:
                return 0
            if (l,r) in dp:
                return dp[(l,r)]
            dp[(l,r)] = 0
            for i in range(l, r+1):
                coins = nums[l-1]*nums[i]*nums[r+1]
                coins += dfs(l, i-1)+dfs(i+1,r)
                dp[(l,r)] = max(coins, dp[(l,r)])
            return dp[(l,r)]
        return dfs(1, len(nums)-2)   # exclude 1 from both side
            
        
# solution from disscussion, accepted and success! performance not impressive         
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        size = len(nums)        
        
        t = [[-1 for j in range(0,size+1)]
            for i in range(0,size+1)]
        
        def solve(l,r):
            if l >= r:
                return 0
            if t[l][r] > 0:
                return t[l][r]

            res = float('-inf')
            for k in range(l,r):
                if t[l][k] != -1:
                    left = t[l][k]
                else:
                    left = solve(l,k)
                    t[l][k] = left

                if t[k+1][r] != -1:
                    right = t[k+1][r]
                else:
                    right = solve(k+1,r)
                    t[k+1][r] = right

                temp = left + right + (nums[l-1]*nums[k]*nums[r])
                res = max(res,temp)
            t[l][r] = res
            return t[l][r]
        return solve(1,size-1)
        
