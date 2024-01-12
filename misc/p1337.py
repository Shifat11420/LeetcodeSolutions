# You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.
# A row i is weaker than a row j if one of the following is true:
# The number of soldiers in row i is less than the number of soldiers in row j.
# Both rows have the same number of soldiers and i < j.
# Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

# Example 1:
# Input: mat = 
# [[1,1,0,0,0],
#  [1,1,1,1,0],
#  [1,0,0,0,0],
#  [1,1,0,0,0],
#  [1,1,1,1,1]], 
# k = 3
# Output: [2,0,3]
# Explanation: 
# The number of soldiers in each row is: 
# - Row 0: 2 
# - Row 1: 4 
# - Row 2: 1 
# - Row 3: 2 
# - Row 4: 5 
# The rows ordered from weakest to strongest are [2,0,3,1,4].

# Example 2:
# Input: mat = 
# [[1,0,0,0],
#  [1,1,1,1],
#  [1,0,0,0],
#  [1,0,0,0]], 
# k = 2
# Output: [0,2]
# Explanation: 
# The number of soldiers in each row is: 
# - Row 0: 1 
# - Row 1: 4 
# - Row 2: 1 
# - Row 3: 1 
# The rows ordered from weakest to strongest are [0,2,3,1].

class Solution:
    # # Time: O(mnlogn), worst case O(nlogn+n*n), Space: O(n)
    # def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    #     m,n = len(mat), len(mat[0])
    #     hm = defaultdict(list)
    #     array = [0]*m
    #     res = []

    #     for i in range(m):
    #         array[i] = mat[i].count(1)
    #         hm[array[i]].append(i)

    #     array.sort()     
    #     for a in set(array):
    #         for i in hm[a]:
    #             res.append(i)
    #             if len(res)==k:
    #                 return res

    # Time: O(mnlogk), Space: O(m)
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m,n = len(mat), len(mat[0])
        minH = []

        for i in range(m):
            heapq.heappush(minH, [mat[i].count(1), i])

        res = []
        for i in range(k):
            res.append(heapq.heappop(minH)[1])
        return res    