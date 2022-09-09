# Given an m x n board of characters and a list of strings words, return all words on the board.
# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

# Example 1:
# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]

# Example 2:
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []


from typing import List
class TrieNode:
    def __init__(self):
        self.children = {}    # hashmap ## character: childnode
        self.IsWord = False

    def addword(self, word):
        cur = self             # rootnode
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.IsWord = True            

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addword(w)        # take each word and to the Trie

        ROWS, COLS = len(board), len(board[0]) 
        visited, res = set(), set()                # we dont wat to return duplicates for res and for visited, we don't want to stuck in infinite loop, dont want to visit same character twice
        
        def dfs(r, c, node, word):                 # word = what word so far, # r,c = coordinated, # node = currently what node from trie     
            if (r<0 or c<0 or r == ROWS or c == COLS or board[r][c] not in node.children or (r,c) in visited):
                return

            visited.add((r,c))
            node = node.children[board[r][c]]   # update node
            word += board[r][c]                 # update character
            if node.IsWord:
                res.add(word)                   # add the string

            dfs(r+1, c, root, word)
            dfs(r-1, c, root, word)
            dfs(r, c+1, root, word)
            dfs(r, c-1, root, word)
            visited.remove((r,c))    # since we are backtracking, we can visit the same one twice. But once we are no longer done visiting it after we return, then we can go ahead and revome this position from being visited

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c, root, "")


        return list(res)     # res is a set, we need a list        