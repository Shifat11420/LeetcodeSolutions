
# According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

def gameOfLife(board):
    r = len(board)
    c = len(board[0])
    neighbors = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    
    
    #counting neighbor sum
    for i in range(r):
        for j in range(c):
            num_ones = 0
            for n in neighbors:
                if 0<= i+n[0]<r and 0<= j+n[1]<c:
                    if board[i+n[0]][j+n[1]]>0:
                        num_ones += 1
            #print("for cell board[",i,j,"] of value", board[i][j], "has nbr sum = ", num_ones )  
            
            # this is done so that calculation does not geet interrupted by value changes
            if board[i][j] == 0 and num_ones ==3:
                board[i][j] = -1
            elif board[i][j] == 1 and (num_ones<2 or num_ones>3):
                board[i][j] = 2
    
    # after all calculationchanges, put the right value in right place
    for i in range(r):
        for j in range(c):   
            if board[i][j] == 2:
                board[i][j] = 0
            if board[i][j] == -1:
                board[i][j] = 1                                    
            
    print(board)
            
    
    
    
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
board = [[1,1],[1,0]]
gameOfLife(board)
  