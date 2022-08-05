#https://leetcode.com/problems/longest-substring-without-repeating-characters/

# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
 
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

#Complexity: time O(n), space O(n) (for set)
# two pointer
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:        
        l = 0
        charSet = set()    # use set to find duplicates
        res = 0

        for r in range(len(s)):
            if s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])    
            res = max(res, r-l+1)
        return res

s = "abcabcbb"
new = Solution
print(new().lengthOfLongestSubstring(s))        

