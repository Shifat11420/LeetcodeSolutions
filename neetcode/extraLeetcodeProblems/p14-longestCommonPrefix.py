# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()

        maxword = strs[-1]
        minword = strs[0]

        i = 0
        prefix = ""
        while i<len(minword):
            if maxword[i]!=minword[i]:
                return prefix
            prefix += minword[i]   
            i += 1   
        return prefix 


strs = ["flower", "flow", "flight"]
new = Solution
print(new().longestCommonPrefix(strs))
