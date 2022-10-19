# Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
# Note:
# Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.
 
# Example 1:
# Input: n = 00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

# Example 2:
# Input: n = 00000000000000000000000010000000
# Output: 1
# Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

# Example 3:
# Input: n = 11111111111111111111111111111101
# Output: 31
# Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
 

# Complexity: time O(32)~ O(1)
# problem is we look at every bit e.g. 1000000001 all of them 0's and 1's
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n%2     # 0 or 1
            n = n>>1       # bit shift  1001 >>1 ----> 100
        return res
    
    
# Complexity: time O(32)~ O(1)
# we look at only bit 1 e.g. 1000000001, just 1's
# subtracting by itself--> getting rid of a bit
# weird trick
class Solution:
    def hammingWeight(self, n: int) -> int:    
        res = 0
        while n:
            n = n & (n-1)
            res += 1
        return res    
    
# still prefer first solution since complexity is same     