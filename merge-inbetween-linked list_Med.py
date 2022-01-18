'''
problem link : https://leetcode.com/problems/merge-in-between-linked-lists/

You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

The blue edges and nodes in the following figure indicate the result:


Build the result list and return its head.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        itr = list1
        count = 0
        
        while itr and count < a-1:
            itr = itr.next
            count += 1
       
        t = itr  # itr at a-1
        
        while t and count < b:
            t = t.next
            count += 1
        
        
        itr.next = list2
        t2 = itr.next
        
        while t2.next:
            t2 = t2.next
        
        t2.next = t.next
                
        return list1
        
       