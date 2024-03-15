# Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.
# A subarray is a contiguous part of the array.

# Example 1:
# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4
# Explanation: The 4 subarrays are bolded and underlined below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]

# Example 2:
# Input: nums = [0,0,0,0,0], goal = 0
# Output: 15

# Constraints:
# 1 <= nums.length <= 3 * 104
# nums[i] is either 0 or 1.
# 0 <= goal <= nums.length

# Time: O(n), Space: O(1)
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def helper(goal):  # to find the num of arrays with sum at most equal to goal
            l = 0
            count, total = 0, 0
            for r, num in enumerate(nums):
                total += num
                while total>goal and l<=r:
                    total -= nums[l]
                    l+=1
                count += r-l+1
            return count 
       
        return helper(goal)-helper(goal-1)           

#  the answer for subarrays of length k
#  must be n−(k−1)=n−k+1
#  since we're able to "start" the array anywhere except for the last k−1 positions.