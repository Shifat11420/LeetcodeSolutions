# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

# Example 1:
# Input: s = "1 + 1"
# Output: 2

# Example 2:
# Input: s = " 2-1 + 2 "
# Output: 3

# Example 3:
# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23

# total stores the running total of the expression evaluated so far,
# num stores the currently processed number, and
# sign stores the sign of the current environment.
# The stack keeps track of nested environments by storing the sign of the previous environment.

# Time : O(n)
class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        total = 0
        sign = 1
        stack = [sign]
        for c in s:
            if c.isdigit():
                num = num*10+int(c)
            elif c == "(":
                stack.append(sign)
            elif c == ")":
                stack.pop()
            elif c == "+" or c == "-":
                total += sign*num
                sign = (1 if c == "+" else -1) * stack[-1]
                num = 0
        return total+sign*num
