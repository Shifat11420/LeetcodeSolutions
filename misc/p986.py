# You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.
# Return the intersection of these two interval lists.
# A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
# The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

# Example 1:
# Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

# Example 2:
# Input: firstList = [[1,3],[5,9]], secondList = []
# Output: []

# Time: O(n+m), Space: O(1)
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        n, m = len(firstList), len(secondList)
        res = []
        
        while i<n and j<m:
            f, s = firstList[i], secondList[j]
            if f[0]<=s[0]<=f[1] or s[0]<=f[0]<=s[1]:
                small, big = max(f[0], s[0]), min(f[1], s[1])
                res.append([small, big])
                if f[1]>big:
                    j+=1
                elif s[1]>big:
                    i+=1
                else:        
                    i+=1
                    j+=1
            elif f[1]<s[0]:
                i+=1
            elif s[1]<f[0]:
                j+=1
        return res                