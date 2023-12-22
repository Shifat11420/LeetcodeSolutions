# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
# Return any possible rearrangement of s or return "" if not possible.

# Example 1:
# Input: s = "aab"
# Output: "aba"

# Example 2:
# Input: s = "aaab"
# Output: ""

# Time: O(nlogk), Space: O(n) 
class Solution:
    def reorganizeString(self, s: str) -> str:
        count= Counter(s)
        maxheap = []
        for key, val in count.items():
            maxheap.append([-val, key])
        heapq.heapify(maxheap)

        res = []
        while len(maxheap)>=2:
            frq1, chr1 = heapq.heappop(maxheap)
            frq2, chr2 = heapq.heappop(maxheap)

            res.extend([chr1, chr2])

            if frq1+1<0:
                heapq.heappush(maxheap, [frq1+1, chr1])
            if frq2+1<0:
                heapq.heappush(maxheap, [frq2+1, chr2])

        if maxheap:
            frq, char = heapq.heappop(maxheap)
            if frq<-1:
                return ""
            res.append(char)
        return "".join(res)