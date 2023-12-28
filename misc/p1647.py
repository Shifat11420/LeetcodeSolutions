# A string s is called good if there are no two different characters in s that have the same frequency.
# Given a string s, return the minimum number of characters you need to delete to make s good.
# The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

# Example 1:
# Input: s = "aab"
# Output: 0
# Explanation: s is already good.

# Example 2:
# Input: s = "aaabbbcc"
# Output: 2
# Explanation: You can delete two 'b's resulting in the good string "aaabcc".
# Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".

# Example 3:
# Input: s = "ceabaacb"
# Output: 2
# Explanation: You can delete both 'c's resulting in the good string "eabaab".
# Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).
 

# Time : O(n+k), Space : O(n+k), n=len(s), k = len(freq)
class Solution:
    def minDeletions(self, s: str) -> int:
        count = {}
        for c in s:
            count[c] = 1 + count.get(c,0)

        freq = [0]*(max(count.values())+1)
        for i in count.values():    
            freq[i]+=1 

        res = 0
        for i in range(len(freq)-1,0,-1):
            v = freq[i]
            if v>1:
                res += v-1
                freq[i-1] += v-1    
        return res

    
    def minDeletions(self, s: str) -> int:
        hm = {}
        count = 0
        for al in set(s):
            temp = s.count(al)
            while temp in hm:
                count += 1
                temp -= 1

            if temp>0:
                hm[temp] = al
        return count        