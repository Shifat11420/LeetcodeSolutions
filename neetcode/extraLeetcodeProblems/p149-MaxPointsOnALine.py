# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

# Example 1:
# Input: points = [[1,1],[2,2],[3,3]]
# Output: 3

# Example 2:
# Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4

# Time : O(n**2)
# Space : O(n)

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        mapping = {}  # slope : freq
        maxinline = 0
        for i in range(n):
            mapping.clear()
            x1, y1 = points[i]
            for j in range(n):
                x2, y2 = points[j]
                if i != j:
                    if abs(x1-x2) == 0:
                        slope = "NO"   # for points in vertical lines
                    else:
                        slope = (y2-y1)/(x2-x1)
                    mapping[slope] = 1 + mapping.get(slope, 0)
            freq = max(mapping.values()) if len(mapping) > 0 else 0
            maxinline = max(freq, maxinline)
        return maxinline+1       # counting the point itself adding 1
