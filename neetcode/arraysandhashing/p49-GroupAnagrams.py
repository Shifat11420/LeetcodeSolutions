# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


from collections import defaultdict
 
## Time Complexity: O(m*n*26)---> O(m*n), m lenth of input list (strs), n is the average of length of the strings, 26 is size of count 
def groupAnagrams(strs):
    res = defaultdict(list) ## mapping charCount to a list of anagrams

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c)-ord("a")] += 1       # ord()--> ASCII characters, ord(c)-ord("a") is a number between 0 to 25

        res[tuple(count)].append(s)           # keys can not be list, so make it a tuple

    return res.values()        


strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))