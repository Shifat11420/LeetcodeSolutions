# https://leetcode.com/problems/delete-nodes-and-return-forest/
# Given the root of a binary tree, each node in the tree has a distinct value.

# After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

# Return the roots of the trees in the remaining forest. You may return the result in any order.

 

# Example 1:


# Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
# Output: [[1,2,null,4],[6],[7]]


class Treenode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def delNodes(self, root:Optional[Treenode], to_delete:List[int]) -> List[Treenode]:
        delete = set(to_delete)
        result = set()
        result.add(root)
        
        def dfs(node):
            if not node:
                return
            
            if node.val in delete:
                if node.left:
                    result.add(node.left)
                if node.right:
                    result.add(node.right)    
            
            dfs(node.left)
            dfs(node.right)
            
            if node.left and node.left.val in delete:
                node.left = None
            if node.right and node.right.val in delete:
                node.right = None    
                
            dfs(root)
            return list(x for x in result if x.val not in delete)    
       
root = [1,2,3,4,5,6,7]
to_delete = [3,5]
Solution.delNodes(root, to_delete)
        