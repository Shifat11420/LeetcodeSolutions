# Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

# Example 1:
# Input: n = 3
# Output: 5

# Example 2:
# Input: n = 1
# Output: 1
 
# Time: O(n^2), Space: O(n)
class Solution:
    def numTrees(self, n: int) -> int:
        cache = {}
        def helper(n):
            if n<=1:
                return 1
            if n in cache:
                return cache[n] 
            total = 0
            for i in range(1,n+1):
                total += helper(i-1)*helper(n-i)       # num of leftsubtrees* num of right subtrees
            cache[n] = total
            return cache[n]
            
        return helper(n)


# Time: O(n^2), Space: O(n)
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1]* (n+1)

        for i in range(2, n+1):
            total = 0
            for j in range(1, i+1):
                total += dp[j-1]*dp[i-j]        
            dp[i] = total
        return dp[n]        