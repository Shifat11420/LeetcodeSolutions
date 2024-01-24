# Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

# Example 1:
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

# Example 2:
# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.

# Example 3:
# Input: nums = [1,2,3]
# Output: 0
 
# Time: O(n), Space: O(n)
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        def factorial(n):
            if n == 1:
                return 1
            return n * factorial(n-1)

        count = Counter(nums)
        total = 0
        for i in count.values():
            if i==1:
                continue
            if i==2:
                total += 1
            else:         
                total += factorial(i) // (2* factorial(i-2))
        return total