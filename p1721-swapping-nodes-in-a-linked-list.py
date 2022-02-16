# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
# You are given the head of a linked list, and an integer k.

# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#using stack
#class Solution:
def swapNodes(head, k):
    s = []
    curr = head
    
    while curr:
        s.append(curr)
        curr = curr.next
        
    s[k-1].val, s[-k].val = s[-k].val, s[k-1].val
    return head    
    
        
        
        
        
        
head = [7,9,6,6,7,8,3,0,9,5]
k = 5        