# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

# The algorithm for myAtoi(string s) is as follows:

# Read in and ignore any leading whitespace.
# Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
# Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
# Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
# If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
# Return the integer as the final result.
# Note:

# Only the space character ' ' is considered a whitespace character.
# Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

#class Solution:
def myAtoi(s: str) -> int:
    MAX_INT = 2**31 - 1 
    MIN_INT = -2**31
    
    
    i = 0
    res = 0
    negative = 1
    
    
    # white space
    while i < len(s) and s[i] == ' ':
        i += 1
    
    # +/- symbol
    if i < len(s) and s[i] == '-':
        i += 1
        negative  = -1
    elif i < len(s) and s[i] == '+':
        i += 1    
        
    # check number 0-9 
    checker = set('0123456789')
    while i < len(s) and s[i] in checker:
        # check MAX MIN int
        if res > MAX_INT / 10 or (res == int(MAX_INT/10) and int(s[i]) > 7 ):
            return MAX_INT if negative  == 1 else MIN_INT
        res = res * 10 + int(s[i])
        i += 1
        
        
    res = res * negative    
    return  res


s = "2147483648"
print(myAtoi(s))    