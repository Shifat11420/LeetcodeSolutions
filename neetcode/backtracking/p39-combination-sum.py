# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

# Example 1:
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.

# Example 2:
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]

# Example 3:
# Input: candidates = [2], target = 1
# Output: []

# two decisions : add a candidate and NOT add the candidate. [2] <-- * --> [], then add 3 to [2], [2,3] <-- [2] --> [2]
# Complexity: O(2**t), each recursion step, we can make 2 decisions and t= target (height of the decision tree, that is, at most the target value)

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, cur, total):    #index, current combination, total of current combination
            if target==total:
                res.append(cur.copy())      #copy because we are going to add to it later
                return
            if i >= len(candidates) or total > target:
                return
            
            # decision to add candidate
            cur.append(candidates[i])
            dfs(i, cur, total+candidates[i])
            
            # decision NOT to add candidate
            cur.pop()
            dfs(i+1, cur, total)
            
        dfs(0, [], 0)
        return res