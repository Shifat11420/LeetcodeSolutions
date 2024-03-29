# Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.
# The test cases are generated so that the answer can fit in a 32-bit integer.

# Example 1:
# Input: nums = [1,2,3], target = 4
# Output: 7
# Explanation:
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# Note that different sequences are counted as different combinations.

# Example 2:
# Input: nums = [9], target = 3
# Output: 0

# Time : O(mn), Space: O(m)
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = {0: 1}

        for total in range(1, target+1):
            cache[total] = 0
            for n in nums:
                cache[total] += cache.get(total-n, 0)
        return cache[target]


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = {}

        def dfs(total):
            if total in cache:
                return cache[total]
            if total == 0:
                return 1
            if total < 0:
                return 0

            cache[total] = 0
            for n in nums:
                cache[total] += dfs(total-n)
            return cache[total]

        return dfs(target)
