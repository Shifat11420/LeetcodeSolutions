# You are given an array of words where each word consists of lowercase English letters.
# wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.
# For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
# A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.
# Return the length of the longest possible word chain with words chosen from the given list of words.

# Example 1:
# Input: words = ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: One of the longest word chains is ["a","ba","bda","bdca"].

# Example 2:
# Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
# Output: 5
# Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].

# Example 3:
# Input: words = ["abcd","dbqca"]
# Output: 1
# Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
# ["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.
 
# Time: O(nm), Space: O(n), n=len(words), m=len(avglen of words)
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        wordset = set(words)
        cache = {}

        def dfs(w):
            if w not in wordset:
                return 0

            if w in cache:
                return cache[w]

            maxchain = 1
            for i in range(len(w)):
                prevword = w[:i]+w[i+1:]
                if prevword in wordset:
                    maxchain = max(maxchain, 1+dfs(prevword))
            cache[w] = maxchain
            return maxchain
        
        return max(dfs(w) for w in words)    



    # # My solution- works but time limit exceeded    
    # def longestStrChain(self, words: List[str]) -> int:
    #     words.sort(key=lambda x:len(x))

    #     def works(s,t):
    #         if len(s)==len(t):
    #             return False
    #         count = 0
    #         i, j = 0, 0
    #         while i<len(s) and j<len(t):
    #             if s[i]!=t[j]:
    #                 count+=1
    #                 j+=1
    #             else:
    #                 while i<len(s) and j<len(t) and s[i]==t[j]:
    #                     i+=1
    #                     j+=1
    #             if i==len(s) and j+1==len(t):
    #                 return True        
    #         return True if count==1 else False
        
    #     adj = defaultdict(list)
    #     for i in range(len(words)):
    #         w1 = words[i]
    #         for j in range(i+1, len(words)):
    #             w2 = words[j]
    #             if len(w2)-len(w1)<=1 and works(w1,w2):
    #                 adj[w1].append(w2)     

    #     visit = set()
    #     res = [words[0]]
    #     maxcount = 1
    #     def dfs(i):
    #         nonlocal maxcount
    #         if i not in adj:
    #             return res
    #         for j in adj[i]:
    #             if j in visit:
    #                 continue
    #             visit.add(j) 
    #             res.append(j)
    #             if dfs(j): 
    #                 c = dfs(j)
    #                 maxcount = max(maxcount, len(c)) 
    #             visit.remove(j)
    #             res.pop()

    #     minlen = len(words[0])
    #     start = []
    #     for w in adj:
    #         if len(w)==minlen:
    #             start.append(w)
    #         if len(w)>minlen:
    #             break          
  
    #     for i in start:  
    #         dfs(i)    
    #     # dfs(words[0])
    #     return maxcount
    