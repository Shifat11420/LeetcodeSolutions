# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

# Example 1:
# Input: s = "the sky is blue"
# Output: "blue is sky the"

# Example 2:
# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.

# Example 3:
# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

class Solution:
    def reverseWords(self, s: str) -> str:
        slist = s.split(" ")
        res = ""
        for i in range(len(slist)-1, -1, -1):
            if slist[i] not in ["", " "]:
                res += str(slist[i])+" "

        return res.strip()

# without split() and strip()


class Solution:
    def reverseWords(self, s: str) -> str:
        i, j = 0, len(s)-1
        res = ""
        while i < j and s[j] == " ":
            j = j-1
        while i < j and s[i] == " ":
            i = i+1

        k = j
        while i <= k:
            wordlength = 0
            if s[k] != " ":
                while i <= k and s[k] != " ":
                    wordlength += 1
                    k = k-1

                res += s[k+1:k+1+wordlength]+" "
            while i <= k and s[k] == " ":
                k = k-1
        return res[:len(res)-1]
