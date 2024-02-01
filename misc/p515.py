# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

# Example 1:
# Input: root = [1,3,2,5,3,null,9]
# Output: [1,3,9]

# Example 2:
# Input: root = [1,2,3]
# Output: [1,3]
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: O(n), Space: O(1)
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = deque([root])
        
        while q:
            maxval = float(-inf)
            for i in range(len(q)):
                node = q.popleft()
                maxval = max(maxval, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(maxval)        
        return res    
