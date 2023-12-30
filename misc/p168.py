# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
# For example:
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
 
# Example 1:
# Input: columnNumber = 1
# Output: "A"

# Example 2:
# Input: columnNumber = 28
# Output: "AB"

# Example 3:
# Input: columnNumber = 701
# Output: "ZY"
 
# Time: O(logN base 26), Space: O(1)
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        c= columnNumber
        s = ""
        while c:
            val = (c-1)%26
            s =  chr(ord("A")+ val)+s
            c = (c-1)//26
        return s

