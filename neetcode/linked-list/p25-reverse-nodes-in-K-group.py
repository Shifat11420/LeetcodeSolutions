# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the list's nodes, only nodes themselves may be changed.

# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]

# Example 2:
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ## dummy node because we eventually modify the head of the list
        ## save 1 node right before our group for 1->2->3 to 1->3->2, 1 is node part of the group
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            # for last group in the list
            if not kth:
                break
            groupNext = kth.next

            # reverse thr group
            prev, curr = kth.next, groupPrev.next
            while curr!= groupNext:
                tmp = curr.next    
                curr.next = prev
                prev = curr
                curr = tmp

            # last step to fix the end points after reversing (like kth becomes the first element)
            tmp = groupPrev.next   # old first node
            groupPrev.next = kth   # new first node
            groupPrev = tmp        # new last node and node before for next group

        return dummy.next     #new head    


    # function to return kth node
    def getKth(self, curr, k):
        while curr and k>0:
            curr = curr.next 
            k -= 1
        return curr        

head = [1,2,3,4,5]
k = 3
new = Solution
print(new().reverseKGroup(head,k))
