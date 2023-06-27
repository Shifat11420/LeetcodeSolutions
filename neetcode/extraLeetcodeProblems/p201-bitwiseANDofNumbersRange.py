# Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

# Example 1:
# Input: left = 5, right = 7
# Output: 4

# Example 2:
# Input: left = 0, right = 0
# Output: 0

# Example 3:
# Input: left = 1, right = 2147483647
# Output: 0

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left != right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift

# 4 =100, 7=111
# 4=>      100 -> 10 -> 1  #right shift of left
# 7=>      111 -> 11 -> 1  #right shift of right
# shift=>    0 -> 1  -> 2  # shift increase by 1 everystep till left==right
# return left<<shift => left =1 -> 10 -> 100 = 4
