# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty. 

# Example 1:
# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".

# Example 2:
# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".

# Example 3:
# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".
 
# Time: O(n), Space: O(1)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def countsymbol(s):
            scount = 0
            for i in range(len(s)):
                if s[i]!="#":
                    scount += 1
                elif scount>0 and i>=scount:
                    scount -= 1
            return scount

        scount = countsymbol(s)
        tcount = countsymbol(t)
        if scount!=tcount:
            return False
        if scount==0:
            return True    

        i, j = len(s)-1, len(t)-1
        slength, tlength = 0, 0

        while i>=0 and j>=0:
            if s[i]=="#" or  t[j]=="#":
                if s[i]=="#":
                    slength += 1 
                    i-=1   
                if t[j]=="#":
                    tlength += 1
                    j-=1 
            elif slength>0 or tlength>0:        
                if slength>0:
                    i-=1           
                    slength-=1
                if tlength>0:
                    j-=1           
                    tlength-=1 
            else:
                if s[i]!=t[j]:
                    return False
                i-=1
                j-=1                
        return True            
        
# Time: O(n), Space: O(n)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:        
        def solve(s):
            stack = []
            for c in s:
                if c!="#":
                    stack.append(c)
                elif stack:
                    stack.pop() 
            return stack

        return solve(s)==solve(t)               