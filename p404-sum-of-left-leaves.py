# https://leetcode.com/problems/sum-of-left-leaves/
# Given the root of a binary tree, return the sum of all left leaves.


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root.left and not (root.left.left) and not (root.left.right):
            return root.left.val + self.sumOfLeftLeaves(root.right)
        else:
            return self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)

