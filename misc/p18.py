# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

# Example 1:
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

# Example 2:
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
 

# Time: O(nlogn+n^3), space O(1)
class Solution:   
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def findsum(l,r,target, N, res, results):
            if (r-l+1<N or N<2 or target<nums[l]*N or target>nums[r]*4):
                return

            
            if N==2:
                while l<r:
                    s = nums[l]+nums[r]
                    if s==target:
                        results.append(res+[nums[l], nums[r]])
                        l+=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                    elif s<target:
                        l+=1
                    else:
                        r-=1
            else:
                for i in range(l,r+1):
                    if i==l or (i>l and nums[i]!=nums[i-1]):
                        findsum(i+1, r, target-nums[i], N-1, res+[nums[i]], results)
                                
        nums.sort()
        results = []
        findsum(0, len(nums)-1, target, 4, [], results)
        return results

   