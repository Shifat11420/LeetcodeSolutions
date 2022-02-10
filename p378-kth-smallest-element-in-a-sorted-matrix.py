# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

# Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# You must find a solution with a memory complexity better than O(n2).



##minheap search
import heapq


matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8

def kthSmallest(matrix, k):
    n = len(matrix)
    visited = [[False for _  in range(n)] for _  in range(n)]

    print(visited)

    minheap = [(matrix[0][0], 0, 0)]
    k = k-1

    print(minheap)

    while minheap:
        ele, x, y = heapq.heappop(minheap)
        if k == 0:
            return ele
        visited[x][y] = True
        if x < n-1 and visited[x+1][y] == False:
            visited[x+1][y] = True
            heapq.heappush(minheap, (matrix[x+1][y], x+1, y))
        if y < n-1 and visited[x][y+1] == False:
            visited[x][y+1] = True
            heapq.heappush(minheap, (matrix[x][y+1], x, y+1))
        k = k-1
        
print(kthSmallest(matrix, k))        