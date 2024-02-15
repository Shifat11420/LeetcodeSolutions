# You are given an integer array nums sorted in non-decreasing order.
# Build and return an integer array result with the same length as nums such that result[i] is equal to the summation of absolute differences between nums[i] and all the other elements in the array.
# In other words, result[i] is equal to sum(|nums[i]-nums[j]|) where 0 <= j < nums.length and j != i (0-indexed).

# Example 1:
# Input: nums = [2,3,5]
# Output: [4,3,5]
# Explanation: Assuming the arrays are 0-indexed, then
# result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4,
# result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3,
# result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5.

# Example 2:
# Input: nums = [1,4,6,8,10]
# Output: [24,15,13,15,21]
 

# Time : O(n), Space: O(n)
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [nums[0]]
        for x in nums[1:]:
            prefix.append(prefix[-1]+x)

        res = []
        for i in range(len(nums)):
            leftsum = prefix[i]-nums[i]
            rightsum = prefix[-1]-prefix[i]

            leftcount = i
            rightcount = n-1-i

            lefttotal = nums[i]*leftcount- leftsum
            righttotal = rightsum - nums[i]*rightcount    

            res.append(lefttotal+righttotal)
        return res    


# Time : O(n), Space: O(1)  
# right partition includes the current term
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftsum = 0
        rightsum = sum(nums)
        res = []
        for i in range(len(nums)):
            leftcount = i
            rightcount = n-i

            lefttotal = nums[i]*leftcount- leftsum
            righttotal = rightsum - nums[i]*rightcount    

            res.append(lefttotal+righttotal)

            leftsum += nums[i]
            rightsum -= nums[i]
        return res            