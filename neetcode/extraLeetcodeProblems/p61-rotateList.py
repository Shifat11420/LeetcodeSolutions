# Given the head of a linked list, rotate the list to the right by k places.

# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

# Example 2:
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        length = 0
        cur = head
        prev = None
        while cur:
            prev = cur
            cur = cur.next
            length += 1

        if k > length:
            k = k % length

        if k == 0 or length == k or length == 1:
            return head

        k = length-k-1
        pointer = head
        while k > 0:
            pointer = pointer.next
            k -= 1

        tmp = pointer.next
        pointer.next = None
        prev.next = head

        return tmp
