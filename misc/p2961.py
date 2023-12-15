# You are given a 0-indexed 2D array variables where variables[i] = [ai, bi, ci, mi], and an integer target.
# An index i is good if the following formula holds:
# 0 <= i < variables.length
# ((aibi % 10)ci) % mi == target
# Return an array consisting of good indices in any order.

# Example 1:
# Input: variables = [[2,3,3,10],[3,3,3,1],[6,1,1,4]], target = 2
# Output: [0,2]
# Explanation: For each index i in the variables array:
# 1) For the index 0, variables[0] = [2,3,3,10], (23 % 10)3 % 10 = 2.
# 2) For the index 1, variables[1] = [3,3,3,1], (33 % 10)3 % 1 = 0.
# 3) For the index 2, variables[2] = [6,1,1,4], (61 % 10)1 % 4 = 2.
# Therefore we return [0,2] as the answer.

# Example 2:
# Input: variables = [[39,3,1000,1000]], target = 17
# Output: []
# Explanation: For each index i in the variables array:
# 1) For the index 0, variables[0] = [39,3,1000,1000], (393 % 10)1000 % 1000 = 1.
# Therefore we return [] as the answer.

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        # create preprocessed hashmap
        prep = {0:[0]}
        for i in range(1,10):
            visit = []
            next_val = i%10
            while next_val not in visit:
                visit.append(next_val)
                next_val = (visit[-1]*i)%10
            prep[i] = visit

        # main calculation, avoid calculating powers
        res = []        
        for i, v in enumerate(variables):
            a,b,c,m = v
            a = a%10
            length = len(prep[a])
            ind = b%length 
            first = prep[a][ind-1]

            s = first%m if c!=1 else first
            while c>1:
                s = (s*first)%m
                c-=1       
            second = s%m

            if second==target:
                res.append(i)
        return res        