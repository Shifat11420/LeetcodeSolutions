# https://leetcode.com/problems/binary-tree-right-side-view/
# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Example 1:
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]

# Example 2:
# Input: root = [1,null,3]
# Output: [1,3]

# Example 3:
# Input: root = []
# Output: []

#DFS
def rightSideView(root):
    values = []
    maxlevel = 0
    
    def dfs(node, level):
        if node:
            if level> maxlevel:
                values.append(node.val)
                maxlevel = level
           
            dfs(node.left,level+1)
            dfs(node.right, level+1)
        return values    
    
    return dfs(root, 1)


#neetcode
#BFS  
import collections
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#BFS
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque([root])
        res = []

        while q:
            rightside = None
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    rightside = node
                    q.append(node.left)
                    q.append(node.right)
            if rightside:
                res.append(rightside.val) 

        return res               
