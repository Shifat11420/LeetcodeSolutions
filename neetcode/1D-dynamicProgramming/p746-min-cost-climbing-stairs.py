# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.

# Example 1:
# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.

# Example 2:
# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: You will start at index 0.
# - Pay 1 and climb two steps to reach index 2.
# - Pay 1 and climb two steps to reach index 4.
# - Pay 1 and climb two steps to reach index 6.
# - Pay 1 and climb one step to reach index 7.
# - Pay 1 and climb two steps to reach index 9.
# - Pay 1 and climb one step to reach the top.
# The total cost is 6.

# can't be greedy and jump 2 steps every time because cost can vary
# brute force O(2^n) , n = len(cost array), 2 brunches of decision tree

# Complexity: time O(n), space O(1) with DP bottom up

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)     #[10,15,20]0
        
        for i in range(len(cost)-3, -1, -1):       # start from 15 in the array and go reverse order
            cost[i] += min(cost[i+1], cost[i+2])   # mincost among 1 step and 2 step taken
            
        return min(cost[0],cost[1])    
            