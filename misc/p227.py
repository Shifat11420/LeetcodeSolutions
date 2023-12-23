# Given a string s which represents an expression, evaluate this expression and return its value. 
# The integer division should truncate toward zero.
# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

# Example 1:
# Input: s = "3+2*2"
# Output: 7

# Example 2:
# Input: s = " 3/2 "
# Output: 1

# Example 3:
# Input: s = " 3+5 / 2 "
# Output: 5

# Time: O(n), Space: O(n)
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        preOp = '+'
        num = 0
        s += '+'

        for c in s:
            if c.isdigit():
                num = 10*num+int(c)
            elif c==" ":
                continue
            else:
                if preOp=="+":
                    stack.append(num)
                elif preOp=="-":
                    stack.append(-num)
                elif preOp=="*":
                    n1 = stack.pop() 
                    stack.append(n1*num)
                elif preOp=="/":
                    n1 = stack.pop() 
                    stack.append(int(n1/num))
                preOp = c
                num = 0
        return sum(stack)            
