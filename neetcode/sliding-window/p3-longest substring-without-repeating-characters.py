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
    def lengthOfLongestSubstring(self, s: str) -> int:  #with set      
        l = 0
        charSet = set()    # use set to find duplicates
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])    
            res = max(res, r-l+1)
        return res

    def lengthOfLongestSubstring(self, s: str) -> int:  #with hm
        hm = {}
        maxlen = 0
        l, r = 0, 0
        while r<len(s):
            if s[r] in hm:
                l = max(l, hm[s[r]])                
            hm[s[r]] = r+1    
            maxlen = max(maxlen, r-l+1)   
            r+=1        
        return maxlen    

s = "abcabcbb"
new = Solution
print(new().lengthOfLongestSubstring(s))        

