# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.

# Example 1:
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

# Example 2:
# Input: root = [1,2]
# Output: 1
 

# for each node there is height (to return value to upper node) and there is diameter (to keep track of maximum)
# height = 1+ max(lefthight, rightheight)
# height(null tree) = -1, height(single node) = 0
# diameter = leftheight + 1 + rightheight + 1 = leftheight + rightheight + 2 

# DFS, starts from bottom
# Complexity: time O(n) - traversing once every node (throught height)
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def dfs(root):
            if not root:
                return -1   #return height

            left = dfs(root.left)
            right = dfs(root.right)

            res[0] = max(res[0], 2+left+right)
            return 1+max(left,right)     #return height

        dfs(root)
        return res[0]      #return diameter