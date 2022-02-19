# You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.

# Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

# 'L' means to go from a node to its left child node.
# 'R' means to go from a node to its right child node.
# 'U' means to go from a node to its parent node.
# Return the step-by-step directions of the shortest path from node s to node t.

 

# Example 1:


# Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
# Output: "UURL"
# Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from collections import defaultdict
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # step 1: build graph
        graph = defaultdict(list)
        stack = [(root)]
        
        
        while stack:
            node = stack.pop()
            if node.left:
                graph[node.val].append((node.left.val, "L"))
                graph[node.left.val].append((node.val, "U"))
                stack.append(node.left)
                
            if node.right:
                graph[node.val].append((node.right.val, "R"))
                graph[node.right.val].append((node.val, "U"))
                stack.append(node.right)

        # step 2: BFS find path
        q = deque([(startValue, "")])
        visited = set()
        visited.add(startValue)
                                   
        while q:
            nodevalue, path = q.popleft()
                 
            if nodevalue == destValue:
                return path                   
                                   
            for neigh in graph[nodevalue]:
                v, d = neigh
                if v not in visited:
                    q.append((v, path+d))
                    visited.add(v)
                                   
        return -1                           
                            