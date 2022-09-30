# Given a string s, return the longest palindromic substring in s.
# A string is called a palindrome string if the reverse of that string is the same as the original string.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"

# start from the middle and check the palindrome outwords in every single position
# Complexity: O(n*n)--> O(n^2)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        reslen = 0
        
        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l>=0 and r < len(s) and s[l]==s[r]:
                if (r-l+1) > reslen:
                    res = s[l:r+1]
                    reslen = r-l+1
                l -= 1
                r += 1
                
            # even length
            l, r = i, i+1
            while l>=0 and r < len(s) and s[l]==s[r]:
                if (r-l+1) > reslen:
                    res = s[l:r+1]
                    reslen = r-l+1
                l -= 1
                r += 1    
        return res      