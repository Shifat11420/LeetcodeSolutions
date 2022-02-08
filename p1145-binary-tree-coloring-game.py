#https://leetcode.com/problems/binary-tree-coloring-game/ 
#Two players play a turn based game on a binary tree. We are given the root of this binary tree, and the number of nodes n in the tree. n is odd, and each node has a distinct value from 1 to n.

# Initially, the first player names a value x with 1 <= x <= n, and the second player names a value y with 1 <= y <= n and y != x. The first player colors the node with value x red, and the second player colors the node with value y blue.

# Then, the players take turns starting with the first player. In each turn, that player chooses a node of their color (red if player 1, blue if player 2) and colors an uncolored neighbor of the chosen node (either the left child, right child, or parent of the chosen node.)

# If (and only if) a player cannot choose such a node in this way, they must pass their turn. If both players pass their turn, the game ends, and the winner is the player that colored more nodes.

# You are the second player. If it is possible to choose such a y to ensure you win the game, return true. If it is not possible, return false.




####three pass solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        
        first = None
        
        
        def count(node):
            nonlocal first
            total = 0
            if node:
                if node.val == x:
                    first = node
                total += count(node.left)+count(node.right)+1
            return total    
        
        s = count(root)
        r = count(first.right)
        l = count(first.left)
        p = s-l-r-1
        
        return l+r<p or l+p<r or r+p<l
            



### onepass solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:

        l,r = None, None
        
        
        def count(node):
            nonlocal l,r
            total = 0
            if node:
                l_count,r_count = count(node.left), count(node.right)
                if node.val == x:
                    l, r = l_count,r_count 
                total += l_count+r_count+1
            return total    
        
        s = count(root)
        p = s-l-r-1
        
        return l+r<p or l+p<r or r+p<l
            
                