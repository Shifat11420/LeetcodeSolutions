# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
## Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        def makeTree(A):
            if A:
                midvalue = len(A)//2
                t = TreeNode(A[midvalue])
                t.left = makeTree(A[:midvalue])
                t.right = makeTree(A[midvalue+1:])
                return t

        A, n = [], head
        while n:
            A.append(n.val)
            n = n.next          
            
        return makeTree(A)