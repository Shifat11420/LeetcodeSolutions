# A parentheses string is valid if and only if:
# It is the empty string,
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
# You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.
# For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
# Return the minimum number of moves required to make s valid.

# Example 1:
# Input: s = "())"
# Output: 1

# Example 2:
# Input: s = "((("
# Output: 3
 

# Time: O(n), Space: O(n)
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        count = 0
        for c in s:
            if c ==")":
                if stack:
                    stack.pop()
                else:
                    count += 1    
            else:
                stack.append(c)
        return len(stack)+count

# Time: O(n), Space: O(1)
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openpar, closepar = 0, 0
        count = 0
        for c in s:
            if c ==")":
                if openpar>0:
                    openpar -= 1
                else:
                    closepar += 1    
            if c == "(":
                openpar += 1        
        return openpar+closepar        