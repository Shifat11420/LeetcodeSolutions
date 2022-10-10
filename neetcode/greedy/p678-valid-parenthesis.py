# Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
# The following rules define a valid string:
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 
# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "(*)"
# Output: true

# Example 3:
# Input: s = "(*))"
# Output: true

# Brute force 3^n, with memoization n^3
# DP, 2D memoization/caching (i, left) --> n^2 matrix, to calculate each value O(n)--> n^3
# left = number of left open parenthesis we have currently
# Greedy O(n), 
# leftMin, leftMax = no of min, max open left parenthesis
# Complexity: time O(n), space O(1)

class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0
        
        for c in s:
            if c=="(":
                leftMin, leftMax = leftMin+1, leftMax+1
            elif c==")":
                leftMin, leftMax = leftMin-1, leftMax-1
            else:                      # wildcard
                leftMin, leftMax = leftMin-1, leftMax+1     #in case, we have ")" and * is chosen "("
            if leftMax < 0:
                return False
            if leftMin <0 :            # (*)( will return true otherwise
                leftMin = 0            # leftMax is still positive and it's valid
        return leftMin == 0