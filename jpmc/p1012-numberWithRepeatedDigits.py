# Given an integer n, return the number of positive integers in the range [1, n] that have at least one repeated digit.

# Example 1:
# Input: n = 20
# Output: 1
# Explanation: The only positive number (<= 20) with at least 1 repeated digit is 11.

# Example 2:
# Input: n = 100
# Output: 10
# Explanation: The positive numbers (<= 100) with atleast 1 repeated digit are 11, 22, 33, 44, 55, 66, 77, 88, 99, and 100.

# Example 3:
# Input: n = 1000
# Output: 262

# Intuition
# Count res the Number Without Repeated Digit
# Then the number with repeated digits = N - res
# Similar as 788. Rotated Digits
# Numbers At Most N Given Digit Set
# Explanation:
# Transform N + 1 to arrayList
# Count the number with digits < n
# Count the number with same prefix
# For example,
# if N = 8765, L = [8,7,6,6],
# the number without repeated digit can the the following format:
# XXX
# XX
# X
# 1XXX ~ 7XXX
# 80XX ~ 86XX
# 870X ~ 875X
# 8760 ~ 8765

# Time Complexity:
# the number of permutations A(m,n) is O(1)
# We count digit by digit, so it's O(logN)

class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
      digits = list(map(int, str(n+1)))
      nl = len(digits)

      res = sum(9*perm(9,i) for i in range(nl-1))

      s = set()
      for i,x in enumerate(digits):
        for y in range(i==0, x):
          if y not in s:
            res += perm(9-i,nl-1-i)
        if x in s:
          break  
        s.add(x)
      return n-res
        