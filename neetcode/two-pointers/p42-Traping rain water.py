#Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
#https://leetcode.com/problems/trapping-rain-water/

from typing import List

# Complexity: time O(n), space O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxleft, maxright = 0, 0
        water = 0

        while l < r:
            if height[l] < height[r]:
                maxleft = max(maxleft, height[l])
                water += maxleft-height[l]
                l += 1
            else:
                maxright = max(maxright, height[r])
                water += maxright-height[r]
                r -= 1
        return water        



height = [0,1,0,2,1,0,1,3,2,1,2,1]
new = Solution
print(new().trap(height))

