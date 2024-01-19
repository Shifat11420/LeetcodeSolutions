# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# Example 1:
# Input: s = "leetcode"
# Output: 0

# Example 2:
# Input: s = "loveleetcode"
# Output: 2

# Example 3:
# Input: s = "aabb"
# Output: -1
 
# # Time: O(n), Space: O(n)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hm = {}
        for i,c in enumerate(s):
            hm[c] = i

        for i,c in enumerate(s):
            if i== hm[c] and s.count(c)==1:
                return i
        return -1            
        
# # Time: O(>n) since count() is O(n), Space: O(1)
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         for i, c in enumerate(s):
#             if s.count(c)==1:
#                 return i
#         return -1                