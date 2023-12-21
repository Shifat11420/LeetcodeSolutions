# Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).
# If two nodes are in the same row and column, the order should be from left to right.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]

# Example 2:
# Input: root = [3,9,8,4,0,1,7]
# Output: [[4],[9],[3,0,1],[8],[7]]

# Example 3:
# Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
# Output: [[4],[9,5],[3,0,1],[8,2],[7]]
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        hm = defaultdict(list)

        def dfs(node, value, level):
            if not node:
                return
            hm[value].append([level,node.val])
            dfs(node.left, value-1, level+1)
            dfs(node.right, value+1, level+1)    
        dfs(root,0, 0)


        res = []
        for key in sorted(hm.keys()):
            newlist = []
            hm[key].sort(key=lambda x:x[0])        
            for level, val in hm[key]:
                newlist.append(val)
            res.append(newlist)
        return res   
        
        
        