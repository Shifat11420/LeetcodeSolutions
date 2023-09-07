# Problem - Partition to K Equal Sum Subsets
# ------------------------------------------------------
# Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

# Example 1:
# Input: nums = [4,3,2,3,5,2,1], k = 4
# Output: true
# Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

# Example 2:
# Input: nums = [1,2,3,4], k = 3
# Output: false

# ------------------------------------------
# Time: O(k*2^n), 2 decisions (include or not), height of tree is n and  k times
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target = sum(nums)//k
        if (sum(nums) % k) != 0:
            return False
        used = [False]*len(nums)
        nums.sort(reverse=True)

        def helper(i, count, subsetsum):
            if k == count:
                return True
            if subsetsum == target:
                return helper(0, count+1, 0)

            for j in range(i, len(nums)):
                if used[j] or subsetsum+nums[j] > target:
                    continue
                if j > i and not used[j-1] and nums[j] == nums[j-1]:
                    continue

                used[j] = True
                if helper(j+1, count, subsetsum+nums[j]):
                    return True
                used[j] = False
            return False

        return helper(0, 0, 0)
