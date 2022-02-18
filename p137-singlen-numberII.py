# https://leetcode.com/problems/single-number-ii/submissions/
# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

# You must implement a solution with a linear runtime complexity and use only constant extra space.


from collections import deque

## two pointer
def singleNumber(nums):
    l = 0
    r = 1
    temp = deque()
    visited = {}
    visited[nums[l]]= 1
    while r < len(nums):
        if nums[l] != nums[r]:
            if nums[r] not in visited:
                temp.append(r)
                visited[nums[r]] = 1
            else:
                visited[nums[r]] += 1                
        else:
            if temp:
                l = temp.popleft()
            visited[nums[r]] += 1 
        r +=1            
    for val,freq in visited.items():
        if freq ==1:
           return val 
            
nums = [2,2,3,2]
print(singleNumber(nums))          