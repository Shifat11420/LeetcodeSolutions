# You are given the head of a singly linked-list. The list can be represented as:
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# Example 1:
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

# Example 2:
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]

# Complexity : time O(n), space O(1)
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]):
        # pointers for finding the half
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        second = slow.next          # second half   
        slow.next = None    # break at half
        prev = None     

        while second:
            tmp = second.next
            second.next = prev
            prev = second             #update
            second = tmp              #update

        # prev is the last node
        # Merge two lists
        first, second = head, prev

        while second:
            tmp1, tmp2 = first.next, second.next          #break the link and save before breaking
            first.next = second          #link
            second.next = tmp1           #link
            first, second = tmp1, tmp2   #update