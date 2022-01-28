#Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
#https://leetcode.com/problems/trapping-rain-water/


# class Solution:
#     def trap(self, height: List[int]) -> int:

def trap(height):
    left , right = 0, len(height)-1        
    water = 0
    maxleft, maxright = 0, 0

    while left < right:
        if height[left] < height[right]:
            maxleft = max (maxleft, height[left])
            water += maxleft - height[left]
            print("water", water)
            left += 1

        else:
            maxright = max(maxright, height[right])
            water += maxright- height[right]    
            print("water", water)
            right -= 1

    print(water)        

#height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,0,3,2,5]
trap(height)

# time O(N)
# space O(1)