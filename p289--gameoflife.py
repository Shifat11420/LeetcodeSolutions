
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
  