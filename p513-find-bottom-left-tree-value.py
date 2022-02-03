
#Given the root of a binary tree, return the leftmost value in the last row of the tree.
# https://leetcode.com/problems/find-bottom-left-tree-value/ 



### BFS implementation --done for understanding the stes for BFS solution####


# # Definition for a binary tree node.
# from collections import deque



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




# def findBottomLeftValue(root):     ## root is a list of treenodes, given
  
#     q = deque([root])            # make a queue out of these treenodes
#     print(q)
#     print("****")

#     res = []
#     if not root:
#         return []

#     while q:
#         node_last = []
#         for i in range(len(q)):
#             node = q.popleft()              #take first element and make a node   
#             print("node only ", node)
#             print("node value ",node.val, "\n")
#             if node.left:
#                 q.append(node.left)
#                 print("q with left :", q)
#             if node.right:
#                 q.append(node.right)
#                 print("q with right :", q)
#             print("final q = ", q, "\n")       
#             node_last.append (node.val)
#             print("node last = ", node_last)
        
#         res.append(node_last)  
#         break                ##no breaks in actual result ,check submitted result
#     print("result = ", res)  
#     print(res[-1][0])
    

# if __name__ == "__main__":
#     root = [1,2,3,4,None,5,6,None,None,7]   
#     a = TreeNode(root[0], root[1], root[2]) 
#     b = TreeNode(root[1], root[3], root[4]) 
#     c = TreeNode(root[2], root[5], root[6]) 
#     d = TreeNode(root[3], root[7], root[8])
#     e = TreeNode(root[5], root[9], None)
#     f = TreeNode(root[6], None, None) 
#     g = TreeNode(root[9], None, None) 

#     root = [a,b,c,d,e,f,g]
#     for i in range(len(root)):
#         findBottomLeftValue(root[i])


    # followed from solution by koalakeys...that is a little different

# #BFS solution

# class Solution:
# def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
# q = deque([root])
# res = []

# if not root:
#     return []

# while q:
#     node_last = []
#     for i in range(len(q)):
#         node = q.popleft()
#         if node.left:
#             q.append(node.left)
#         if node.right:
#             q.append(node.right)
#         node_last.append(node.val)
        
#     res.append(node_last)    

# return res[-1][0]



##DFS solution
def findBottomLeftValue(root):
    def dfs(node,depth):
        if node.left == None and node.right == None:
            return [depth, node.value]
        if node.left == None:
            return dfs(node.right, depth+1)
        if node.right == None:
            return dfs(node.left, depth+1)

        left = dfs(node.left, depth+1)
        right = dfs(node.right, depth+1)

        return left if left[0]>=right[0] else right    #left[0], right[0] are depths
            
    print(dfs(root,0)[1])
    return dfs(root,0)[1]



