# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.


nums = [5,7,8,8,8,8,8,9,10]
target = 8

def searchRange( nums, target):
    start = 0
    end = len(nums)-1
    targetlist = []
    
        
    
    while start <= end:            
        if start==end:
            if nums[start] == target:
                return [start,end]
        mid = start + (end-start)//2
        
        if nums[mid] == target:
            temp = mid
            while nums[mid] == target and mid >=start:
                targetlist.append(mid)
                mid = mid-1

            while nums[temp] == target and temp < end:
                temp = temp+1 
                if nums[temp] == target:
                    targetlist.append(temp)
            return [min(targetlist),max(targetlist)]               
        
        if nums[start]<= target and target <nums[mid]:
            end = mid
        else:
            start = mid+1
            
            
    if targetlist == []:
        targetlist.append(-1)            
        return [min(targetlist),max(targetlist)]                    


print(searchRange( nums, target))