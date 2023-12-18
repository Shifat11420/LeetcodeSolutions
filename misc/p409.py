# Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.
# Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

# Example 1:
# Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
# Output: 2

# Example 2:
# Input: board = [["."]]
# Output: 0

class Solution:
    
    #Time : O(mn), Space: O(mn)
    # def countBattleships(self, board: List[List[str]]) -> int:
    #     ROW, COL = len(board), len(board[0])
    #     visit =set()
    #     directions = [[-1,0],[1,0],[0,1],[0,-1]]
        
    #     def bfs(r,c):
    #         q= deque()
    #         q.append((r,c))
    #         visit.add((r,c))

    #         while q:
    #             for i in range(len(q)):
    #                 row, col = q.popleft()
    #                 for dr,dc in directions:
    #                     r,c =row+dr, col+dc
    #                     print("inside ", r, c)
    #                     if (r<0 or r==ROW or c<0 or c==COL or (r,c) in visit or board[r][c]=="."):
    #                         continue
    #                     q.append((r,c))
    #                     visit.add((r,c))  
                    
    #     noOfBattleships = 0
    #     for r in range(ROW):
    #         for c in range(COL):
    #             if board[r][c]=="X" and (r,c) not in visit:
    #                 bfs(r,c)
    #                 noOfBattleships += 1
    #     return noOfBattleships

    #Time : O(mn), Space: O(1)
    def countBattleships(self, board: List[List[str]]) -> int:
        ROW, COL = len(board), len(board[0])
        count = 0
        for r in range(ROW):
            for c in range(COL):
                if board[r][c]=="X":
                    if r-1>=0 and board[r-1][c]=="X":
                        continue
                    if c-1>=0 and board[r][c-1]=="X":
                        continue
                    count += 1        

        return count            