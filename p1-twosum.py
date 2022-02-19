#https://leetcode.com/problems/two-sum/

#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up 
# to target.You may assume that each input would have exactly one solution, and you may not use the same 
# element twice.You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## using hash O(n)
        
        mapping = {}
        
        for i in range(len(nums)):
            if target-nums[i] in mapping:
                return [i, mapping[target-nums[i]]]
            mapping[nums[i]] = i
    
