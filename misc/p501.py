# Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.
# If the tree has more than one mode, return them in any order.
# Assume a BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees. 

# Example 1:
# Input: root = [1,null,2,2]
# Output: [2]

# Example 2:
# Input: root = [0]
# Output: [0]
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: O(n), Space: O(n)
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, count):
            if not node:
                return
            count[node.val] = 1+ count.get(node.val, 0)    
            dfs(node.left, count)
            dfs(node.right, count)
            return count
        count = dfs(root, {}) 

        maxOcc = max(count.values())
        res = []
        for k, v in count.items():
            if v == maxOcc:
                res.append(k)
        return res        

# Time: O(n), Space: O(1)
# Inorder, no hash map
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:        
        prev, cur, maxO, res = None, 0, 0, []
        
        def dfs(node):
            if not node:
                return
            nonlocal prev, cur, maxO, res    

            dfs(node.left)
            
            if node.val==prev:
                cur += 1
            else:
                prev = node.val
                cur = 1

            if cur==maxO:
                res.append(node.val)
            elif cur>maxO:
                res.clear()
                res.append(node.val)
                maxO=cur

            dfs(node.right)

        dfs(root)
        return res