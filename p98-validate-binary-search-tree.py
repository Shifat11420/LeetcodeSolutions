# https://leetcode.com/problems/validate-binary-search-tree/

# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import inf

## DFS and recursion
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, leftB, rightB):
            if not node:
                return True
            if not (leftB <node.val and node.val < rightB):
                return False
            return (valid(node.left, leftB, node.val) and valid(node.right, node.val, rightB))
        
        return valid(root, float(-inf), float(inf))