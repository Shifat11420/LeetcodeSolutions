# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
# the smallest in lexicographical order
#  among all possible results.

# Example 1:
# Input: s = "bcabc"
# Output: "abc"

# Example 2:
# Input: s = "cbacdcbc"
# Output: "acdb"

# Time: O(n), Space: O(n)
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lastOcc = {}
        for i,c in enumerate(s):
            lastOcc[c] = i

        stack = []
        visit = set()
        for i, c in enumerate(s):
            if c not in visit:
                while stack and c < stack[-1] and i < lastOcc[stack[-1]]:
                    chr = stack.pop()
                    visit.remove(chr) 
                visit.add(c)
                stack.append(c)
        return "".join(stack)        
