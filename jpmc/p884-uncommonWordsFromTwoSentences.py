# A sentence is a string of single-space separated words where each word consists only of lowercase letters.
# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
# Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

# Example 1:
# Input: s1 = "this apple is sweet", s2 = "this apple is sour"
# Output: ["sweet","sour"]

# Example 2:
# Input: s1 = "apple apple", s2 = "banana"
# Output: ["banana"]

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        l1 = s1.split(" ")
        l2 = s2.split(" ")

        mapp = {}
        for w in l1:
            mapp[w] = 1+mapp.get(w,0)
        for w in l2:
            mapp[w] = 1+mapp.get(w,0)

        res = []          
        for w in mapp.keys():
            if mapp[w]==1:
                res.append(w)    
        return res