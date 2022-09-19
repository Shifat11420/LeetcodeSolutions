# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
# A palindrome string is a string that reads the same backward as forward.

# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]

# Example 2:
# Input: s = "a"
# Output: [["a"]]

# bruteforce, backtracking
# check every single partition and check if they are palindrome,add them and recursively continue DFS (add rest of the charaters in the tree)
# if they are not partition, leave that choice, this way they will not make palindromes
#  Complexity: O(2^n) at least

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []   #list of partitions
        
        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            
            for j in range(i, len(s)):         # in the same level of the tree
                if self.isPalindrome(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)                   # this basically shows in the next step of dfs which index it's starting at
                    part.pop()
                    
        dfs(0)
        return res
    
    def isPalindrome(self, s, l, r):
        while l<r:
            if s[l]!=s[r]:
                return False
            l, r = l+1, r-1        
        return True     