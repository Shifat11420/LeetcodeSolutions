# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
# Given an integer n, return the nth ugly number

# Example 1:
# Input: n = 10
# Output: 12
# Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

# Example 2:
# Input: n = 1
# Output: 1
# Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
 
# Time: O(n), Space: O(n)
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        arr = [0]*n
        arr[0] = 1
        a=b=c=0

        for i in range(1,n):
            l1, l2, l3 = arr[a]*2, arr[b]*3, arr[c]*5
            arr[i] =  min(l1, l2, l3)
            if arr[i]==l1: a+=1
            if arr[i]==l2: b+=1
            if arr[i]==l3: c+=1
        return arr[n-1]
  