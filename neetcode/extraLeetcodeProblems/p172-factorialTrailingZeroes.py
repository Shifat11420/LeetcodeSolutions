# Given an integer n, return the number of trailing zeroes in n!.
# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

# Example 1:
# Input: n = 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.

# Example 2:
# Input: n = 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.

# Example 3:
# Input: n = 0
# Output: 0

# To compute the number of trailing zeroes in n!, we need to count the number of factors of 10 in n!. Notice that 10 can only be formed by multiplying 2 and 5, and we can always find more factors of 2 than factors of 5 in n!. Therefore, it suffices to count the number of factors of 5 in n! to determine the number of trailing zeroes.

# Time : O(logn)
# Space : O(1)
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n > 0:
            count += n//5
            n = n//5
        return count
