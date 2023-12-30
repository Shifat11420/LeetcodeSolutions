# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

# Example 1:
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

# Example 2:
# Input: s = "Mr Ding"
# Output: "rM gniD"
 
# Time : O(n), Space : O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        return " ".join([w[::-1] for w in words])

    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        for i,w in enumerate(words):
            l,r = 0, len(w)-1
            wlist = list(w)

            while l<=r:
                wlist[l], wlist[r] = wlist[r], wlist[l]
                l+=1
                r-=1
            words[i] = "".join(wlist)          
        return " ".join(words) 