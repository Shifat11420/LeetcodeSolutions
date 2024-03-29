# Problem - 473. Matchsticks to Square
# ------------------------------------------------------------------
# You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

# Return true if you can make this square and false otherwise.

# Example 1:
# Input: matchsticks = [1,1,2,2,2]
# Output: true
# Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.

# Example 2:
# Input: matchsticks = [3,3,3,3,4]
# Output: false
# Explanation: You cannot find a way to form a square with all the matchsticks.
# -------------------------------------------------------
# Time: O(4^n)
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        length = sum(matchsticks)//4

        if sum(matchsticks)/4 != length:
            return False
        sides = [0]*4

        matchsticks.sort(reverse=True)

        def backtrack(i):
            if i == len(matchsticks):
                return True

            for j in range(4):
                if sides[j]+matchsticks[i] <= length:
                    sides[j] += matchsticks[i]
                    if backtrack(i+1):
                        return True
                    sides[j] -= matchsticks[i]
            return False

        return backtrack(0)
