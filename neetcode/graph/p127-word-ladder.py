# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

# Example 1:
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

# Example 2:
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

# BFS, adjacency list
# Complexity: n^2*m overall

# creating adjacency list with nested loop in the entire list:  n= number of words<=5000, m = length of each word<=10, n^2*m  -changed to--> m^2*n
# hot --> *ot or h*t or ho*  patterns, n*m*m  (going through every pattern = n, going through every single character we removed = m, add each word to the list = m)
# BFS : n^2*m (n^2, n= no of edges we potentially have and m for comparing the words)

import collections
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # build adjacency list
        nei = collections.defaultdict(list)  
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):    
                pattern = word[:j]+"*"+word[j+1:]       # skipping jth character and putting *
                nei[pattern].append(word)

        # BFS
        visit = set([beginWord])
        q = collections.deque([beginWord])    
        res = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):    
                    pattern = word[:j]+"*"+word[j+1:] 
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0    


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
new = Solution
print(new().ladderLength(beginWord, endWord, wordList))