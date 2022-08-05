# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.
# A substring is a contiguous sequence of characters within the string.

# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

# Example 2:
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.

# Example 3:
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.


#Complexity : time O(n)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, reslen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # adding to "have" so that we can have a string containong all of t string
            if c in countT and countT[c] == window[c]:
                have += 1

            while have == need:   ## we have what we need, i. e. required string is there, now check the length
                ## update result
                if (r-l+1) < reslen:
                    res = [l, r]
                    reslen = r - l +1

                ## pop from the left of the window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:   # if anything poped was a character od t, decrease 'have' and go to next for loop
                    have -= 1
                l += 1
        l, r = res        
        return s[l:r+1] if reslen != float("infinity") else ""            

s = "ADOBECODEBANC"
t = "ABC"        
new = Solution
print(new().minWindow(s,t))