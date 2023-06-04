# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
# You should preserve the original relative order of the nodes in each of the two partitions.

# Example 1:
# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]

# Example 2:
# Input: head = [2,1], x = 2
# Output: [1,2]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        low_head = low_tail = ListNode(0)
        high_head = high_tail = ListNode(0)

        cur = head
        while cur:
            if cur.val<x:
                low_tail.next = cur
                low_tail = low_tail.next
            else:
                high_tail.next = cur
                high_tail = high_tail.next
            cur = cur.next

        high_tail.next = None
        low_tail.next = high_head.next
        return low_head.next   