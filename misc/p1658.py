# You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.
# Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

# Example 1:
# Input: nums = [1,1,4,2,3], x = 5
# Output: 2
# Explanation: The optimal solution is to remove the last two elements to reduce x to zero.

# Example 2:
# Input: nums = [5,6,7,8,9], x = 4
# Output: -1

# Example 3:
# Input: nums = [3,2,20,1,1,3], x = 10
# Output: 5
# Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.

# Time : O(n), Space: O(1)
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        total = sum(nums)
        target = total - x

        if target==0:
            return n
        if target<0:
            return -1    

        minNum = float(inf)
        left, right = 0, 0 
        cursum = 0
        while right<n:
            cursum += nums[right]
            right += 1

            while cursum>target and left<n:
                cursum -= nums[left]
                left += 1

            if target==cursum:
                minNum = min(minNum, len(nums)-(right-left))
        return -1 if minNum==float(inf) else minNum            