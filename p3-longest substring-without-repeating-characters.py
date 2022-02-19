#https://leetcode.com/problems/longest-substring-without-repeating-characters/

# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
 
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:        
        i= 0
        ans = 0
        mp = {}
        for j in range(len(s)):
            if s[j] in mp:
                i = max(i,mp[s[j]])
            mp[s[j]]= j+1
            ans = max(ans,j-i+1)
        return ans    

