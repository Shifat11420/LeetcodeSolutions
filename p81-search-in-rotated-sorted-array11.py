
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

# There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

# Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

# Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

# You must decrease the overall operation steps as much as possible.



###binarysearch
nums = [2,5,6,0,0,1,2]
target = 0

def search(nums, target):
    start = 0
    end = len(nums)-1
    
    
    while start<end: 
        mid = start+ (end-start)//2      
        if nums[mid] == target:
            return True
        
        if nums[start] < nums[mid]:  #firstpartsorted
            if nums[start]<= target and target < nums[mid]: #search in sorted
                end  = mid
            else:
                start = mid+1
            
        elif nums[start] > nums[mid]:  #lastpartsorted
            if nums[mid]<target and target<=nums[end]: #search in sorted
                start = mid+1
            else:                
                end = mid
        else:   
            start += 1
    return nums[start]==target


print(search(nums, target))                   
    
    