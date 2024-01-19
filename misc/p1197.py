# In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].
# A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.
# Return the minimum number of steps needed to move the knight to the square [x, y]. It is guaranteed the answer exists.

# Example 1:
# Input: x = 2, y = 1
# Output: 1
# Explanation: [0, 0] → [2, 1]

# Example 2:
# Input: x = 5, y = 5
# Output: 4
# Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
 
# Time: O(1), Space: O(1)
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        if x<y:
            x,y = y,x
        if x==1 and y==0:
            return 3
        if x==2 and y==2:
            return 4 

        delta = x-y

        if y>delta:
            return delta - 2 * ((delta-y)//3)
        else:           
            return delta - 2 * ((delta-y)//4)

# Time: O(n), Space: O(n)
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        dp = {}
        def dfs(x,y):
            key = x*1000+y
            if key in dp:
                return dp[key]
            if x+y==0:
                return 0
            if x+y==2:
                return 2              
            dp[key] = min(dfs(abs(x-2),abs(y-1)), dfs(abs(x-1),abs(y-2))) + 1
            return dp[key]   

        return dfs(abs(x),abs(y))
