# Given a string s, find the longest palindromic subsequence's length in s.
# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

# Example 1:
# Input: s = "bbbab"
# Output: 4
# Explanation: One possible longest palindromic subsequence is "bbbb".

# Example 2:
# Input: s = "cbbd"
# Output: 2
# Explanation: One possible longest palindromic subsequence is "bb".
 

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.longestCommonSubsequence(s, s[::-1])

    def longestCommonSubsequence(self, s1, s2):
        m, n = len(s1), len(s2)
        row = [0]*(n+1) 

        for i in range(m-1,-1,-1):
            currow = [0]*(n+1)
            for j in range(n-1, -1, -1):
                if s1[i]==s2[j]:
                    currow[j] = 1 + row[j+1]
                else:
                    currow[j] = max(currow[j+1], row[j])
            row = currow
        return currow[0]  