#  https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/ 
# You are given the root of a binary tree with n nodes, where each node is uniquely assigned a value from 1 to n. You are also given a sequence of n values voyage, which is the desired pre-order traversal of the binary tree.

# Any node in the binary tree can be flipped by swapping its left and right subtrees. For example, flipping node 1 will have the following effect:


# Flip the smallest number of nodes so that the pre-order traversal of the tree matches voyage.

# Return a list of the values of all flipped nodes. You may return the answer in any order. If it is impossible to flip the nodes in the tree to make the pre-order traversal match voyage, return the list [-1].




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        self.index = -1
        self.output = []
        
        def preorder(root):
            
            if root:
                self.index +=1
                if root.val != voyage[self.index]:
                    self.output = [-1]
                    return
               
                if root.left and root.left.val != voyage[self.index+1]:
                    root.left, root.right = root.right, root.left
                    self.output.append(root.val)
                preorder(root.left)
                preorder(root.right)
        
        preorder(root)    
            
        return [-1] if -1 in self.output else self.output     