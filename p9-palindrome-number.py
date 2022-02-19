#https://leetcode.com/problems/palindrome-number/
# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward.

# For example, 121 is a palindrome while 123 is not.
 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.


def isPalindrome(x: int):
    length =  len(str(x))
 
    for i in range(length//2):
        if not str(x)[i] == str(x)[-(i+1)]:
            return False
    return True        
    
    
    
    
print(isPalindrome(66851215666))   