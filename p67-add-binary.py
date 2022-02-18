# https://leetcode.com/problems/add-binary/
# Given two binary strings a and b, return their sum as a binary string.


def addBinary(a,b):
    added = binaryTOdecimal(a) + binaryTOdecimal(b)
    return decimalTObinary(added)

def binaryTOdecimal(val):
    n = len(val)-1
    result = 0
    for i in range(len(val)):
        result += int(val[i])* 2**n
        n -= 1    
    return result   

def decimalTObinary(val):
    remainder = ""
    if val == 0:
        return "0"
    while val >=1:
        remainder += str(val%2)
        val = val//2    
    return remainder[::-1]     
    
a = "1010"
b = "1011"    
print(addBinary(a,b))
