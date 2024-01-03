# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

# Example 1:
# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.

# Example 2:
# Input: s = "aba"
# Output: false

# Example 3:
# Input: s = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 
# Time: O(n*sqrt(n)), Space: O(n)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n//2+1):
            if n%i==0:
                pattern = s[:i]*(n//i)
                if pattern==s:
                    return True
        return False  

# Time: O(n), Space: O(n)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        t= s+s
        if s in t[1:-1]:
            return True
        return False                     
        