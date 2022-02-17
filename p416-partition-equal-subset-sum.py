# https://leetcode.com/problems/partition-equal-subset-sum/

# Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

#dynamic programming and memoization, DFS

def canPartition(nums):
    cache = set()
    def dfs(target,nums):
        if target < 0 :
            return False
        if target == 0:
            return True 
        
        
        if target in cache:
            return False
        cache.add(target)
        
        for index, num in enumerate(nums):
            if dfs(target-num, nums[index+1:]) or dfs(target, nums[index+1:]):
                return True
        return False 
    
    sum_nums = sum(nums)
    if sum_nums % 2 != 0:
        return False
    return dfs(sum_nums//2, nums)   
    
    
    
nums = [1,2,3,5]
print(canPartition(nums))    