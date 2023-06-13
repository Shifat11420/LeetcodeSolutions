# Given the head of a singly linked list, return true if it is a
# palindrome
#  or false otherwise.

# Example 1:
# Input: head = [1,2,2,1]
# Output: true

# Example 2:
# Input: head = [1,2]
# Output: false

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        stack = []
        count = 0

        cur = head
        while cur:
            count += 1
            cur = cur.next

        p1 = head
        half = count//2
        for i in range(half):
            stack.append(p1.val)
            p1 = p1.next
        if count % 2:
            p1 = p1.next

        while p1:
            if not stack or p1.val != stack.pop():
                return False
            p1 = p1.next
        return True
