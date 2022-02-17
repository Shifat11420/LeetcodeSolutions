 # problem description
 # file:///home/shifat/Pictures/Screenshot%20from%202022-02-17%2012-08-47.png
 
## Multi-source BFS
## linear time complexity --O(n)

 
import queue
from tkinter.tix import ROW


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        ROWS, COLS = len(rooms), len(rooms[0])
        q = queue()
        visited = set()
        
        def addRoom(r,c):
            if (r<0 or r==ROWS or c<0 or c==COLS or rooms[r][c]==-1 or (r,c) in visited):
                return
            visited((r,c))
            q.append([r,c])        
        
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    visited.add((r,c))
                    q.append([r,c])
                    
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()            
                rooms[r][c] = dist
                addRoom(r+1,c)
                addRoom(r-1,c)
                addRoom(r,c+1)
                addRoom(r,c-1)
            dist +=1