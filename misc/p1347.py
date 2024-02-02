# You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.
# Return the minimum number of steps to make t an anagram of s.
# An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

# Example 1:
# Input: s = "bab", t = "aba"
# Output: 1
# Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.

# Example 2:
# Input: s = "leetcode", t = "practice"
# Output: 5
# Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.

# Example 3:
# Input: s = "anagram", t = "mangaar"
# Output: 0
# Explanation: "anagram" and "mangaar" are anagrams. 
 
# Time: O(s+t), Space: O(s+t)
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        countS = Counter(s)
        countT = Counter(t)

        res = 0
        for c in countT:
            x = countS.get(c,0)
            if countT[c]>=x:
                res += countT[c]- x
        return res

# Time: O(s+t), Space: O(t)
class Solution:
    def minSteps(self, s: str, t: str) -> int:        
        res = 0
        for c in set(t):
            tt = t.count(c)
            ss = s.count(c)
            if tt>=ss:
                res += tt-ss
        return res 