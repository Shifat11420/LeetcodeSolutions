# Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:
# Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
# Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.
# In other words, we treat '(' as an opening parenthesis and '))' as a closing parenthesis.
# For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.
# You can insert the characters '(' and ')' at any position of the string to balance it if needed.
# Return the minimum number of insertions needed to make s balanced.

# Example 1:
# Input: s = "(()))"
# Output: 1
# Explanation: The second '(' has two matching '))', but the first '(' has only ')' matching. We need to add one more ')' at the end of the string to be "(())))" which is balanced.

# Example 2:
# Input: s = "())"
# Output: 0
# Explanation: The string is already balanced.

# Example 3:
# Input: s = "))())("
# Output: 3
# Explanation: Add '(' to match the first '))', Add '))' to match the last '('.

# Time: O(n), Space : O(1)
class Solution:
    def minInsertions(self, s: str) -> int:
        s = s.replace('))','}')
        miss_br = 0
        req_cl = 0

        for c in s:
            if c=='(':
                req_cl += 2
            else:
                if c==')':
                    miss_br += 1
                if req_cl:
                    req_cl -= 2
                else:
                    miss_br += 1
        return miss_br + req_cl       