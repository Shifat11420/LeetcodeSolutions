# Given an integer n, return the number of prime numbers that are strictly less than n.

# Example 1:
# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

# Example 2:
# Input: n = 0
# Output: 0

# Example 3:
# Input: n = 1
# Output: 0

# Time: O(n*log(log(n))), Space: O(n)
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<3: 
            return 0
        
        arr = [1]*n
        arr[0] = arr[1] = 0
        m = 2
        while m*m<n:
            if arr[m]==1:
                # for i in range(m*m, n, m):
                #     arr[i] = 0
                arr[m*m:n:m] = [0] * (1+ (n-m*m-1)//m)   #saving memory and make code faster
            m += 1 if m==2 else 2        
        return sum(arr)            

# arithmatic sequence formula
# an = a1 + (n-1)*d
# n = 1 + (an-a1)/d
# n = 1 + (n-1-m*m)/m        