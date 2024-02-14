# You are given two integer arrays nums1 and nums2. We write the integers of nums1 and nums2 (in the order they are given) on two separate horizontal lines.
# We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:
# nums1[i] == nums2[j], and
# the line we draw does not intersect any other connecting (non-horizontal) line.
# Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).
# Return the maximum number of connecting lines we can draw in this way.

# Example 1:
# Input: nums1 = [1,4,2], nums2 = [1,2,4]
# Output: 2
# Explanation: We can draw 2 uncrossed lines as in the diagram.
# We cannot draw 3 uncrossed lines, because the line from nums1[1] = 4 to nums2[2] = 4 will intersect the line from nums1[2]=2 to nums2[1]=2.

# Example 2:
# Input: nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
# Output: 3

# Example 3:
# Input: nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
# Output: 2

class Solution:
    # Memoization # Time: O(mn), Space: O(mn), #m = len(rows), n= len(cols)
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        cache = {}
        def dfs(i,j):
            if (i, j) in cache:
                return cache[(i,j)]
            if i==len(nums1) or j==len(nums2):
                return 0
            if nums1[i]==nums2[j]:
                cache[(i,j)] = 1 + dfs(i+1, j+1)
            else:
                cache[(i,j)] = max(dfs(i+1, j), dfs(i, j+1))    
            return cache[(i, j)]
        return dfs(0,0)    

    # Dynamic programming # Time: O(mn), Space: O(mn), #m = len(rows), n= len(cols)
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0]* (len(nums2)+1) for _ in range(len(nums1)+1)]

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        return dp[len(nums1)][len(nums2)]                 


    
    # Dynamic programming optimized # Time: O(mn), Space: O(n), #m = len(rows), n= len(cols)
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [0]* (len(nums2)+1) 

        for i in range(len(nums1)):
            newdp = [0]* (len(nums2)+1) 
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    newdp[j+1] = 1 + dp[j]
                else:
                    newdp[j+1] = max(newdp[j], dp[j+1])
            dp = newdp        
        return dp[len(nums2)]    