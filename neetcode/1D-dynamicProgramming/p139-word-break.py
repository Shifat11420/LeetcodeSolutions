# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# Example 1:
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

# Example 2:
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.

# Example 3:
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false

# s = 'leetcode', w = 'leet'
# dp[8]= dp[0+len(w)]=dp[4]=True
# Complexity: O(n*m*n), n = len(s) (go through every single position), m = len(wordDict), n for matching
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)   # 1 for base case
        dp[len(s)] = True           # base case
        
        for i in range(len(s)-1, -1, -1): # go reverse
            for w in wordDict:
                if i+len(w) <= len(s) and s[i:i+len(w)]==w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:                 # if it's true, no need to check anymore, go to next iteration
                    break
                    
        return dp[0]            
                
    
        