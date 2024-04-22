# Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

# Example 1:
# Input: n = 3
# Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

# Example 2:
# Input: n = 1
# Output: [[1]]

# Constraints:
# 1 <= n <= 8

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: O(n*n), Space: O(n)
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def dfs(nums):
            if not nums:
                return [None]

            ans = []
            for i in range(len(nums)):
                lefttrees = dfs(nums[:i])
                righttrees = dfs(nums[i+1:])

                for l in lefttrees:
                    for r in righttrees:
                        root = TreeNode(nums[i])    
                        root.left = l
                        root.right = r
                        ans.append(root)
            return ans
        nums = list(range(1,n+1))  
        return dfs(nums)