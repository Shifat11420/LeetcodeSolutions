# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

# Complexity: time O(n), space O(1)
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        count1, count2 = {}, {}
        for c in range(len(s1)):
            count1[s1[c]] = 1 + count1.get(s1[c],0)    
            count2[s2[c]] = 1 + count2.get(s2[c],0)

        if count1 == count2:
            return True

        l = 0
        window = len(s1)
        for r in range(window, len(s2)):
            count2[s2[l]] -= 1
            if count2[s2[l]] == 0:
                count2.pop(s2[l])
            count2[s2[r]] = 1 + count2.get(s2[r],0)
            if count1 == count2:
                return True
            l += 1     
        return False
            
s1 = "ab"
s2 = "eidbaooo"
new = Solution
print(new().checkInclusion(s1, s2))    
    