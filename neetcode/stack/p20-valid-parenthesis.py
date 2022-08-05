# https://leetcode.com/problems/valid-parentheses/
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false



##O(n) time, O(n) space for stack
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToopen = {'}':'{', ')':'(', ']':'['}
        
        for c in s:
            if c in closeToopen:
                if stack and stack[-1]==closeToopen[c]:
                    stack.pop()
                else:    
                    return False    
            else:
                stack.append(c)
        return True if not stack else False            

new = Solution
s = "()[[]{}"
print(new().isValid(s))