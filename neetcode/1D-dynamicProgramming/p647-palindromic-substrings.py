# Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.

# Example 1:
# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".

# Example 2:
# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

# Complexity: time O(n*n)+O(n*n)---> O(n^2) (for odd n*n and even n*n where starting every single position and going outward to the end-->n and doing it for every single character --->n)

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        for i in range(len(s)):
            l = r = i
            while l>=0 and r<len(s) and s[l]==s[r]:
                res += 1
                l -= 1
                r += 1

            l, r = i, i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                res += 1
                l -= 1
                r += 1
        return res        
            