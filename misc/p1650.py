# Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).
# Each node will have a reference to its parent node. The definition for Node is below:
# class Node {
#     public int val;
#     public Node left;
#     public Node right;
#     public Node parent;
# }
# According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)." 

# Example 1:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.

# Example 2:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5 since a node can be a descendant of itself according to the LCA definition.

# Example 3:
# Input: root = [1,2], p = 1, q = 2
# Output: 1
 
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""
# Time: O(n), Space: O(n), n=height of the tree
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def ancestors(node):
            stack = []
            while node:
                stack.append(node)
                node = node.parent
            return stack

        stack1, stack2 = ancestors(p), ancestors(q) 

        LCA = None
        while stack1 and stack2 and stack1[-1]==stack2[-1]:
            LCA = stack1[-1]
            stack1.pop()
            stack2.pop()
        return LCA    

# Time: O(n), Space: O(1), n=height of the tree
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def ancestors(node):
            depth = 0
            while node:
                depth += 1
                node = node.parent
            return depth

        depth1, depth2 = ancestors(p), ancestors(q) 

        for i in range(abs(depth1-depth2)):
            if depth1>depth2:
                p = p.parent
            else:
                q = q.parent

        while p!=q:
            p = p.parent
            q = q.parent
        return p
                   