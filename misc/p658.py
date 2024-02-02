# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.
# An integer a is closer to x than an integer b if:
# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b
 
# Example 1:
# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]

# Example 2:
# Input: arr = [1,2,3,4,5], k = 4, x = -1
# Output: [1,2,3,4]

# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
#         minH = []
#         for a in arr:
#             heapq.heappush(minH, [abs(a-x), a])
#         res = []
#         while minH and k>0:
#             d, point = heapq.heappop(minH)    
#             res.append(point)
#             k-=1
#         res.sort()    
#         return res


# Time: O(logn), Space: O(1)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr)-k

        while l<r:
            m = (l+r)//2
            if x<= (arr[m]+arr[m+k])/2:
                r = m
            else:
                l = m+1
        return arr[l:l+k]    