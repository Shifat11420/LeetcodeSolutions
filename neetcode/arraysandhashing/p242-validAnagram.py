# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

from typing import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashmap solution, 
        # time O(s+t) -> iterate through both strings,
        # space O(s+t) -> two hashmaps
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True        

        # builtin counter solution, 
        # time O(s+t) -> iterate through both strings,
        # space O(s+t) -> two hashmaps

        return Counter(s) == Counter(t)

        # builtin sort solution, 
        # time O(s+t) -> iterate through both strings,
        # space O(1) 

        return sorted(s) == sorted(t)