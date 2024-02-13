# You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.
# A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.
# Return the length longest chain which can be formed.
# You do not need to use up all the given intervals. You can select pairs in any order.

# Example 1:
# Input: pairs = [[1,2],[2,3],[3,4]]
# Output: 2
# Explanation: The longest chain is [1,2] -> [3,4].

# Example 2:
# Input: pairs = [[1,2],[7,8],[4,5]]
# Output: 3
# Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].

# Time: O(n), Space: O(1)
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x:x[1])

        longest = 1
        current = 1
        lastpair = pairs[0]
        for i in range(1, len(pairs)):
            if lastpair[1]<pairs[i][0]:
                current += 1
                longest = max(longest, current)
                lastpair = pairs[i]
        return longest        
        