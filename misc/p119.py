# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:
# Input: rowIndex = 3
# Output: [1,3,3,1]

# Example 2:
# Input: rowIndex = 0
# Output: [1]

# Example 3:
# Input: rowIndex = 1
# Output: [1,1]
 
# Time: O(n*n), Space: O(n*n)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = {i: [1]*(i+1) for i in range(rowIndex+1)}
        for row in range(2, rowIndex+1):
            for i in range(1,len(dp[row])-1):
                dp[row][i] = dp[row-1][i-1]+dp[row-1][i]
        # print(dp)
        return dp[rowIndex]


# Time: O(n*n), Space: O(n) -- space optimized
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [1]*(rowIndex+1)
        for row in range(2, rowIndex+1):
            nextdp = [1]*(rowIndex+1)
            for i in range(1, row):
                nextdp[i] = dp[i-1]+dp[i]
            dp = nextdp    
        return dp    
