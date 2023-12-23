# You are given an encoded string s. To decode the string to a tape, the encoded string is read one character at a time and the following steps are taken:
# If the character read is a letter, that letter is written onto the tape.
# If the character read is a digit d, the entire current tape is repeatedly written d - 1 more times in total.
# Given an integer k, return the kth letter (1-indexed) in the decoded string.

# Example 1:
# Input: s = "leet2code3", k = 10
# Output: "o"
# Explanation: The decoded string is "leetleetcodeleetleetcodeleetleetcode".
# The 10th letter in the string is "o".

# Example 2:
# Input: s = "ha22", k = 5
# Output: "h"
# Explanation: The decoded string is "hahahaha".
# The 5th letter is "h".

# Example 3:
# Input: s = "a2345678999999999999999", k = 1
# Output: "a"
# Explanation: The decoded string is "a" repeated 8301530446056247680 times.
# The 1st letter is "a".

# Time: O(n), Space: O(1)
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
        for c in s:
            if c.isdigit():
                size *= int(c)
            else:
                size += 1
        print(size)

        for c in reversed(s):
            if c.isdigit():
                size = size//int(c)
                k = k%size
            else:
                if k==0 or k==size:
                    return c
                size -= 1   
            print(size, k)                     
      