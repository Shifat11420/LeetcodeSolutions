# 11. Container With Most Water
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

# https://leetcode.com/problems/container-with-most-water/
# class Solution:
#     def maxArea(self, height: List[int]) -> int:

#Complexity: time O(n)
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        res = 0

        while l<r:
            area = (r-l) * min(height[l], height[r])
            res = max(area, res)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1    
        return res

height =  [1,8,6,2,5,4,8,3,7]   
new = Solution
print(new().maxArea(height))        