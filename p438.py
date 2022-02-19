# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

import collections
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_dict = collections.Counter(s[:len(p)-1])
        p_dict = collections.Counter(p)
        
        start = 0
        res = []
        
        for i in range(len(p)-1, len(s)):
            s_dict[s[i]] += 1
            
            if s_dict == p_dict:
                res.append(start)
        
            s_dict[s[start]] -= 1
            
            if s_dict[s[start]] == 0:
                del s_dict[s[start]]
            start += 1
        return res