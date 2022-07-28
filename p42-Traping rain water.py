#Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
#https://leetcode.com/problems/trapping-rain-water/

from typing import List

# Complexity: time O(N), space O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        left , right = 0, len(height)-1        
        water = 0
        maxleft, maxright = 0, 0

        while left < right:
            if height[left] < height[right]:
                maxleft = max (maxleft, height[left])
                water += maxleft - height[left]
                left += 1

            else:
                maxright = max(maxright, height[right])
                water += maxright- height[right]    
                right -= 1

        return water
    

height = [0,1,0,2,1,0,1,3,2,1,2,1]
new = Solution
print(new().trap(height))

