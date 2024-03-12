# Given a string s, return the length of the longest repeating substrings. If no repeating substring exists, return 0.

# Example 1:
# Input: s = "abcd"
# Output: 0
# Explanation: There is no repeating substring.

# Example 2:
# Input: s = "abbaba"
# Output: 2
# Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.

# Example 3:
# Input: s = "aabcaabdaab"
# Output: 3
# Explanation: The longest repeating substring is "aab", which occurs 3 times.
 
# Constraints:
# 1 <= s.length <= 2000
# s consists of lowercase English letters.

# Time: O(n(n-L)logn), Space: O(n(n-L))
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)
        def hasdup(length):
            seen = set()
            for start in range(n-length+1):
                if s[start:start+length] in seen:
                    return True
                seen.add(s[start:start+length])
            return False

        l, r = 1, n
        while l<=r:
            m = (l+r)//2
            if hasdup(m):
                l = m+1
            else:
                r = m-1
        return r               
        