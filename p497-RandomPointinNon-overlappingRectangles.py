# https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/
# You are given an array of non-overlapping axis-aligned rectangles rects where rects[i] = [ai, bi, xi, yi] indicates that (ai, bi) is the bottom-left corner point of the ith rectangle and (xi, yi) is the top-right corner point of the ith rectangle. Design an algorithm to pick a random integer point inside the space covered by one of the given rectangles. A point on the perimeter of a rectangle is included in the space covered by the rectangle.

# Any integer point inside the space covered by one of the given rectangles should be equally likely to be returned.

# Note that an integer point is a point that has integer coordinates.

# Implement the Solution class:

# Solution(int[][] rects) Initializes the object with the given rectangles rects.
# int[] pick() Returns a random integer point [u, v] inside the space covered by one of the given rectangles.


import bisect
import random


# class Solution:
    
#     def numPoints(self, rect):
#         x1, y1, x2, y2 = rect
#         return (x2 - x1 + 1) * (y2 - y1 + 1)

#     def __init__(self, rects):
#         self.rects = rects
#         self.presum = [0]
#         for i in range(len(rects)):
#             self.presum.append(self.presum[-1] + self.numPoints(rects[i]))

#     def pick(self):
#         n =  random.randint(1, self.presum[-1])
#         i = bisect.bisect_left(self.presum, n) 
#         n -= self.presum[i-1]
#         x1, y1, x2, y2 = self.rects[i-1]
#         q, r = divmod(n, x2 - x1 + 1)
#         if r:
#             return [x1 + r -1, y1 + q]
#         return [x2, y1 + q -1]
    
# solution = Solution([[-2, -2, 1, 1], [2, 2, 4, 6]])
# solution.pick() 


def numPoints(rect):
    x1, y1, x2, y2 = rect
    return (x2 - x1 + 1) * (y2 - y1 + 1)
rects = [[-2, -2, 1, 1], [2, 2, 4, 6]]

presum = [0]
for i in range(len(rects)):
    presum.append(presum[-1] + numPoints(rects[i]))
print("presum = ",presum)

n =  random.randint(1, presum[-1])
i = bisect.bisect_left(presum, n) 

print("n, i = ",n,i)
n -= presum[i-1]
x1, y1, x2, y2 = rects[i-1]
print("x1, y1, x2, y2 = ",x1, y1, x2, y2)

print("updated n, i = ",n,i)
q, r = divmod(n, x2 - x1 + 1)
print("q,r : ",q,r)

if r:
    print([x1 + r -1, y1 + q])
else:    
    print([x2, y1 + q -1])