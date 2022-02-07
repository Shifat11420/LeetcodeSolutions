#You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.
# https://leetcode.com/problems/recover-binary-search-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


    
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []
        val = []
        
        def inorder(node):
            if node:
                inorder(node.left)
                nodes.append(node)
                val.append(node.val)
                inorder(node.right)
            
        inorder(root)    
            
        print(val)    
            
        n = len(nodes)    
        left, right = 0, n-1
        
        while left < n-1 and nodes[left].val < nodes[left+1].val:
            left += 1
        while right > 0 and nodes[right].val > nodes[right-1].val:
            right -= 1
            
        nodes[left].val, nodes[right].val = nodes[right].val, nodes[left].val    #swap
            