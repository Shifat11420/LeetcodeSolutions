# 11. Container With Most Water
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# https://leetcode.com/problems/container-with-most-water/
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         length = len(height)

def maxArea(height):
    left = 0
    right = len(height)-1

    maxarea = 0

    while left < right:
        area = (right - left) * min(height[left],height[right])
        maxarea = max(maxarea, area)

        print (left, right, height[left], height[right], area,  maxarea)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return maxarea        




height =  [1,8,6,2,5,4,8,3,7]   
print(maxArea(height))