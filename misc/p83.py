# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Example 1:
# Input: head = [1,1,2]
# Output: [1,2]

# Example 2:
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
 
# Time: O(n), Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        cur = head
        nxt = cur.next
        while nxt:
            if cur.val==nxt.val:
                while nxt and cur.val==nxt.val:
                    nxt = nxt.next
                cur.next = nxt
            cur = cur.next
            if nxt:
                nxt = nxt.next        
        return head