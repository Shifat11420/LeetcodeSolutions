# Given a string s, return the number of homogenous substrings of s. Since the answer may be too large, return it modulo 109 + 7.
# A string is homogenous if all the characters of the string are the same.
# A substring is a contiguous sequence of characters within a string.

# Example 1:
# Input: s = "abbcccaa"
# Output: 13
# Explanation: The homogenous substrings are listed as below:
# "a"   appears 3 times.
# "aa"  appears 1 time.
# "b"   appears 2 times.
# "bb"  appears 1 time.
# "c"   appears 3 times.
# "cc"  appears 2 times.
# "ccc" appears 1 time.
# 3 + 1 + 2 + 1 + 3 + 2 + 1 = 13.

# Example 2:
# Input: s = "xy"
# Output: 2
# Explanation: The homogenous substrings are "x" and "y".

# Example 3:
# Input: s = "zzzzz"
# Output: 15

# Time : O(n), Space : O(1)
class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9+7
        i, j = 0, 0
        total = 0
        while i<len(s) and j<len(s):
            length = 0
            while j<len(s) and s[i]==s[j]:
                j+=1
            length = j-i 
            total += (length*(length+1)//2)%MOD 
            i = j
        return total

