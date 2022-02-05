from numpy import transpose, array

def boardcheck(board):
    rowdict = {}
    newdict = {}
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] in rowdict:
                rowdict[board[i][j]] += 1
            else:
                rowdict[board[i][j]] = 1   


        for key in rowdict:
            if (not key == ".") and rowdict[key] >1: 
                print("here False")
                return False     
        
        rowdict = {} 
    return True  

def iterateM(mat):
    matdict = {}
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] in matdict:
                matdict[mat[i][j]] += 1
            else:
                matdict[mat[i][j]] = 1   

    for key in matdict:
        if (not key == ".") and matdict[key] >1: 
           return False     
    return True    

def isValidSudoku(board):
    boardTrans = transpose(board)        

    start = 3  
    board = array(board)
    for i in range(3):
        for j in range(3):
            chunkM = board[start*i:3*(i+1),start*j:3*(j+1)]
            if boardcheck(chunkM) == False or iterateM(chunkM) == False:
                return False
            

    
    if not (boardcheck(board) == True and boardcheck(boardTrans) == True):
        return False
    return True
                







boardA =[
    ["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

boardB = [
 ["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

boardC = [
    [".",".",".",".","5",".",".","1","."],
    [".","4",".","3",".",".",".",".","."],
    [".",".",".",".",".","3",".",".","1"],
    ["8",".",".",".",".",".",".","2","."],
    [".",".","2",".","7",".",".",".","."],
    [".","1","5",".",".",".",".",".","."],
    [".",".",".",".",".","2",".",".","."],
    [".","2",".","9",".",".",".",".","."],
    [".",".","4",".",".",".",".",".","."]]

print(isValidSudoku(boardC))


### other solution
import collections
def isValidSudoku1(board):
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    squares = collections.defaultdict(set)
 

    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                continue
            if(board[i][j] in rows[i] or
                board[i][j] in cols[j] or
                board[i][j] in squares[(i//3 , j//3)]):
                return False
            rows[i].add(board[i][j])
            cols[j].add(board[i][j])
            squares[(i//3 , j//3)].add(board[i][j])
            print(rows)
            print(cols)
            print(squares)
    return True

print(isValidSudoku1(boardA))    