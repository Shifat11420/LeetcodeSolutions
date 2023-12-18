# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

# Example 1:
# Input: s = "aba"
# Output: true

# Example 2:
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.

# Example 3:
# Input: s = "abc"
# Output: false
class Solution:
    # def validPalindrome(self, s: str) -> bool:
    #     flag = False

    #     def dfs(l,r,flag):   
    #         if abs(r-l)<=1 and s[l]==s[r]:
    #             return True
    #         if s[l]==s[r]:
    #             return dfs(l+1,r-1, flag)
    #         if s[l]!=s[r] and not flag:
    #             flag = True
    #             return dfs(l+1,r, flag) or dfs(l,r-1, flag)    
    #         return False
    #     return dfs(0,len(s)-1, flag)    


    # Time: O(n), Space: O(1)
    def validPalindrome(self, s: str) -> bool:    
        l, r = 0, len(s)-1

        while l<=r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                skipl, skipr = s[l+1:r+1], s[l:r]    
                return skipl==skipl[::-1] or skipr==skipr[::-1]
        return True        


        