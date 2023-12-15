# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

# Example 1:
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]

# Example 2:
# Input: head = []
# Output: []

# Example 3:
# Input: head = [1]
# Output: [1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:      
        dummy = ListNode(0, head)
        prev = dummy
        cur = head

        while cur and cur.next:
            tmp = cur.next.next
            prev.next = cur.next
            cur.next.next = cur
            cur.next = tmp

            prev = cur
            cur = cur.next
   
        return dummy.next    

    # Generalized Solution for k =2
    #     dummy = ListNode(0, head)
    #     groupPrev = dummy

    #     while True:
    #         kth = self.getkth(groupPrev, 2)
    #         if not kth:
    #             break
    #         groupNext = kth.next

    #         prev, cur = kth.next, groupPrev.next  
    #         while cur!= groupNext:
    #             tmp = cur.next
    #             cur.next = prev
    #             prev = cur
    #             cur = tmp

    #         tmp = groupPrev.next
    #         groupPrev.next = kth
    #         groupPrev = tmp
    #     return dummy.next

    # def getkth(self, cur, k):
    #     while cur and k>0:
    #         cur = cur.next
    #         k -= 1
    #     return cur
              



