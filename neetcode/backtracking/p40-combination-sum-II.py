# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.

# Example 1:
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]

# Example 2:
# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]

# Idea: we sort the array and ignore duplicates in the iteration, not down the tree
# Complexity: O(2^n), n= size of candidates

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def backtrack(cur, pos, target):   #cur = current combination, pos = starting position, target = current target after decreasing everytime
            # base case
            if target == 0:
                res.append(cur.copy())
                return
            if target <= 0:
                return
                
            prev = -1    
            for i in range(pos, len(candidates)):
                if prev == candidates[i]:
                    continue
                cur.append(candidates[i])
                backtrack(cur, i+1, target-candidates[i])
                cur.pop()
                
                prev = candidates[i]
                
        backtrack([], 0, target) 
        return res