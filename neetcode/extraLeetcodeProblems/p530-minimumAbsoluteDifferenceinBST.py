# Since the inorder traversal of a BST returns the node values in ascending order, we can traverse the tree in inorder and keep track of the previous visited node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        minvalue = float("inf")
        prev = None

        def inorder(node):
            nonlocal minvalue, prev
            if not node:
                return
            inorder(node.left)
            if prev:
                minvalue = min(minvalue, abs(node.val-prev.val))
            prev = node
            inorder(node.right)

        inorder(root)
        return minvalue
