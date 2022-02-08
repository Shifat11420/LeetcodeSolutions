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
                            