# Given a positive integer n, find the pivot integer x such that:
# The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
# Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.

# Example 1:
# Input: n = 8
# Output: 6
# Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.

# Example 2:
# Input: n = 1
# Output: 1
# Explanation: 1 is the pivot integer since: 1 = 1.

# Example 3:
# Input: n = 4
# Output: -1
# Explanation: It can be proved that no such integer exist.
 
# Constraints:
# 1 <= n <= 1000

# Time: O(n+logn), Space: O(1)
class Solution:
    def pivotInteger(self, n: int) -> int:
        def summ(i,j):
            total = 0
            for k in range(i, j+1):
                total += k
            return total

        if n==1:
            return 1
        l, r = 1, n
        while l<r:
            m = (l+r)//2
            if summ(1,m-1)>summ(m+1,n):
                r = m-1
            elif summ(1,m-1)<summ(m+1,n): 
                l = m+1
            else:
                return m
        return -1               
        

# Time: O(n), Space: O(1)
class Solution:
    def pivotInteger(self, n: int) -> int:        
        nums = range(1,n+1)
        total = sum(nums)
        currentsum = 0
        for num in nums:
            currentsum += num
            if currentsum==total:
                return num
            total -= num
        return -1    