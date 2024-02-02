# You are given an array of strings products and a string searchWord.
# Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.
# Return a list of lists of the suggested products after each character of searchWord is typed.

# Example 1:
# Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
# Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
# Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
# After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
# After typing mou, mous and mouse the system suggests ["mouse","mousepad"].

# Example 2:
# Input: products = ["havana"], searchWord = "havana"
# Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
# Explanation: The only word "havana" will be always suggested while typing the search word.
 
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.words = list()
        self.n = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addword(self, word):
        cur = self.root      
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c] 

            if cur.n<3:
                cur.words.append(word)
                cur.n += 1

    def searchbyPrefix(self, prefix):
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return ''
            cur = cur.children[c]
        return cur.words                                

# Time : O(plogp), Space: O(26)~O(1)
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        P = products
        P.sort()
        trie = Trie()

        for word in P:
            trie.addword(word)

        cur = ''
        res = []
        for s in searchWord:
            cur += s
            res.append(trie.searchbyPrefix(cur))
        return res        