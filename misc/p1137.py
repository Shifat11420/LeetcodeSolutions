# The Tribonacci sequence Tn is defined as follows: 
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# Given n, return the value of Tn.

# Example 1:
# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4

# Example 2:
# Input: n = 25
# Output: 1389537
 
# Time: O(n), Space: O(1)
class Solution:
    def tribonacci(self, n: int) -> int:
        if n<2:
            return n
        if n==2:
            return 1     

        zero, one, two = 0, 1, 1 
        for i in range(3, n+1):
            i = zero+one+two
            zero = one
            one = two
            two = i
        return two    

# just a bit nicer :)
# Time: O(n), Space: O(1)
class Solution:
    def tribonacci(self, n: int) -> int:        
        t = [0, 1, 1]
        if n<3:
            return t[n]
        for i in range(3, n+1):
            tmp =  t[2]+t[1]+t[0]    
            t[0] = t[1]
            t[1] = t[2]
            t[2] = tmp
        return t[2]    
