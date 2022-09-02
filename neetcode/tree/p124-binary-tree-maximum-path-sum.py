# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
# The path sum of a path is the sum of the node's values in the path.
# Given the root of a binary tree, return the maximum path sum of any non-empty path.

# Example 1:
# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

# Example 2:
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

# DFS, recursive 
#  Complexity : time : O(n),space O(logn) , height of the tree is logn


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# consider splitting for tracking maximum parth sum and without splitting for returning path
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]   # Global variable, list because we can modify in the recursive function
        
        # return max path sum without split
        def dfs(root):
            if not root:
                return 0

            leftmax = dfs(root.left)
            rightmax = dfs(root.right)

            # update for not considering negatives
            leftmax = max(leftmax, 0)
            rightmax = max(rightmax, 0)

            res[0] = max(res[0], root.val + leftmax + rightmax)        #keeps track of the global maximum path sum
            return root.val + max(leftmax, rightmax)

        dfs(root)
        return res[0]    
