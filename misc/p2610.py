# You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:
# The 2D array should contain only the elements of the array nums.
# Each row in the 2D array contains distinct integers.
# The number of rows in the 2D array should be minimal.
# Return the resulting array. If there are multiple answers, return any of them.
# Note that the 2D array can have a different number of elements on each row.

# Example 1:
# Input: nums = [1,3,4,1,2,3,1]
# Output: [[1,3,4,2],[1,3],[1]]
# Explanation: We can create a 2D array that contains the following rows:
# - 1,3,4,2
# - 1,3
# - 1
# All elements of nums were used, and each row of the 2D array contains distinct integers, so it is a valid answer.
# It can be shown that we cannot have less than 3 rows in a valid array.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: [[4,3,2,1]]
# Explanation: All elements of the array are distinct, so we can keep all of them in the first row of the 2D array.
 

# # Time: O(n^2), Space: O(n)
# class Solution:
#     def findMatrix(self, nums: List[int]) -> List[List[int]]:
#         count = {}
#         for n in nums:
#             count[n] = 1+ count.get(n, 0)
        
#         res = []
#         while len(count)>0:
#             arr = []
#             for i in list(count):
#                 arr.append(i)
#                 count[i]-=1   
#                 if count[i]==0:
#                     count.pop(i)
#             res.append(arr)        
#         return res    

# Time: O(n), Space: O(n)
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = [0]* (len(nums)+1)
        ans = []

        for c in nums:
            if freq[c]>=len(ans):
                ans.append([])

            ans[freq[c]].append(c)
            freq[c] += 1
        return ans    