# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

# Example 1:
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true

# Example 2:
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false

#Complexity: time O(root+subroot)
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False    # root null but subroot not null
        if self.sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right, subRoot))    

    def sameTree(self, s, t):
        if not s and not t:
            return True
        if s and t and (s.val == t.val):
            return self.sameTree(s.left,t.left) and self.sameTree(s.right, t.right)
        return False             