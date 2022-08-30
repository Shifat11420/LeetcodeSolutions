# https://leetcode.com/problems/validate-binary-search-tree/
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Example 1:
# Input: root = [2,1,3]
# Output: true

# Example 2:
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
 

# Complexity: time O(n) --- O(2n)-> O(n) for 2 comparisons in each node
## DFS and recursion
from math import inf
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, leftB, rightB):
            if not node:
                return True
            if not (leftB <node.val and node.val < rightB):
                return False
            return (valid(node.left, leftB, node.val) and valid(node.right, node.val, rightB))    # when go left, update right boundary, when go right update left boundary
        
        return valid(root, float(-inf), float(inf))