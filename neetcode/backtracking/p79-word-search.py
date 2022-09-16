# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example 1:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

# Example 2:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true

# Example 3:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false


# Complexity: (without added code)
#             O(n * m * complexity of dfs) = O(n*m*4^t), 
#             n and m = dimensions of board, 
#             complexity of dfs = len(word)= t and called 4 times, so 4^t   
#             (with added code probably also adds n * m)

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        
        ######### without this part of code, solution is not efficient  ##########
        if len(word) > ROW * COL:    
            return False                

        path = set()
        for r in range(ROW):
            for c in range(COL):
                path.add(board[r][c])
        if len(path) < len(set(word)):          
            return False                        
        #################################################################

        def dfs(r, c, i):   # i = index of current position in the word
            if i == len(word):
                return True
            if (r<0 or c<0 or r==ROW or c==COL or (r,c) in path or word[i]!=board[r][c]):
                return False
            
            path.add((r,c))
            res = (dfs(r+1, c, i+1) or
                  dfs(r-1, c, i+1) or
                  dfs(r, c+1, i+1) or
                  dfs(r, c-1, i+1))
            path.remove((r,c))          # since we are returning from this function, we are no longer visiting this path    
            return res
        
        for r in range(ROW):
            for c in range(COL):
                if dfs(r,c,0): return True
        return False        
            
        
        
