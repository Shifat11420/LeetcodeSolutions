# https://leetcode.com/problems/binary-tree-right-side-view/
# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.


#DFS

def rightSideView(root):
    values = []
    maxlevel = 0
    
    def dfs(node, level):
        if node:
            if level> maxlevel:
                values.append(node.val)
                maxlevel = level
           
            dfs(node.left,level+1)
            dfs(node.right, level+1)
        return values    
    
    return dfs(root, 1)