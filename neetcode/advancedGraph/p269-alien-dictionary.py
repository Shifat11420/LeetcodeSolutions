# There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

# Example 1:
# Input:
# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]
# Output: "wertf"

# Example 2:
# Input:
# [
#   "z",
#   "x"
# ]
# Output: "zx"

# Example 3:
# Input:
# [
#   "z",
#   "x",
#   "z"
# ]

# Output: "" 

# Explanation: The order is invalid, so return "".
# Note:
# You may assume all letters are in lowercase.
# You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return any one of them is fine.

# topological sort
# graph that uses directed edges but no cycles
# DFS with workaround --> postorder DFS, leaf nodes first, do this in reverse order
# loop detection-- visit, path (if node is visited-FALSE, if node in current path-TRUE)

# Complexity: O(no of characters)

from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:   
        # create adjacency list
        adj = {c:set() for w in words for c in w}
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minlen = min(len(w1), len(w2))
            if len(w1)>len(w2) and w1[:minlen] == w2[:minlen]:
                return ""
            for j in range(minlen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        # DFS
        visit = {}      # False = visited, True = current path
        res = []    
        def dfs(c):
            if c in visit:               # loop detection
                return visit[c]

            visit[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visit[c] = False   
            res.append(c) 

        for c in adj:
            if dfs(c):        # loop detection
                return ""  
        res.reverse()
        return "".join(res)        

words = [
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
new = Solution
print(new().alienOrder(words))