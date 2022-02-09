# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


            
            
#DFS
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = defaultdict(list)
    
        def dfs(node,key):         
            if node:
                level[key].append(node.val)
                                 
                if node.left:dfs(node.left,key+1)
                if node.right:dfs(node.right,key+1)
          
            
        dfs(root,0) 
        return level.values()
            
        
        
         
## level order traversal

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:       
        if not root:
            return []
        stack = []
        queue = [root]  

        while queue:        
            stack.append([node.val for node in queue])
            l = []
            for node in queue:
                if node.left:
                    l.append(node.left)
                if node.right:
                    l.append(node.right)
            queue = l   
            print("queue : ",queue)
        return stack           