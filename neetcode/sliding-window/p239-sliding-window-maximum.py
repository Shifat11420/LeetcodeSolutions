# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.

# Example 1:
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

# monotonically decreasing queue, deque
# reason for using queue, not stack is, we want to add and remove from the beginning
# Complexity : time O(n), space O(n)

import collections
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()  #index
        l = r = 0
        output = []

        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left value from window
            if l > q[0]:
                q.popleft()

            if r+1 >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output            

nums = [1,3,-1,-3,5,3,6,7]
k = 3
new = Solution
print(new().maxSlidingWindow(nums, k))      
