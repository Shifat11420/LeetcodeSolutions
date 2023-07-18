# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]

# Example 2:
# Input: head = [5], left = 1, right = 1
# Output: [5]

# Time : O(n)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev = None
        cur = head
        count = 1
        prevLeft = None
        rightNext = None


        while cur:
            if count<left:
                prevLeft = cur
            if count == left:
                listLeft = cur
            if count == right:
                listRight = cur
                rightNext = cur.next
            if count>= left and count<=right:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp            
            else:
                prev = cur
                cur = cur.next
            count += 1

        listLeft.next = rightNext

        if prevLeft==None:
            return listRight
        else:    
            prevLeft.next = listRight
        return head    