# For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

# Example 1:
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"

# Example 2:
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"

# Example 3:
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
 
# Time: O((l1+l2)*l2), Space : O(l1+l2) 
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)
        res = ""
        reslen = -1
        for i in range(1, l2+1):
            if l2%i==0 and l1%i==0:
                reslen = i
                pattern1 = str2[:i] * (l1//i)            
                pattern2 = str2[:i] * (l2//i)
                if pattern1 == str1 and pattern2 ==str2:
                    reslen = i
                    res = str2[:i]
        return res         

# Time: O(n), Space : O(n), length of larger strings
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ""
        if len(str1) == len(str2):
            return str1
        if len(str1)>len(str2):    
            return self.gcdOfStrings(str1[len(str2):], str2)    
        return self.gcdOfStrings(str1, str2[len(str1):])            