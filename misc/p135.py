# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
# You are giving candies to these children subjected to the following requirements:
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.

# Example 1:
# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

# Example 2:
# Input: ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
# The third child gets 1 candy because it satisfies the above two conditions.
 
# Constraints:
# n == ratings.length
# 1 <= n <= 2 * 104
# 0 <= ratings[i] <= 2 * 104


# Time: O(n), Space: O(n)
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candys = [1]*n
        for i in range(1, len(ratings)):
            if ratings[i]>ratings[i-1]:
                candys[i] = 1+candys[i-1]

        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                candys[i] = max(candys[i], 1+candys[i+1])         
        
        return sum(candys)


# Time: O(n), Space: O(1)
class Solution:
    def candy(self, ratings: List[int]) -> int:
        up, down, peak = 0, 0, 0
        res = 1

        for prev, cur in zip(ratings[:-1], ratings[1:]):
            if prev<cur:
                up, down, peak = 1+up, 0, 1+up
                res += 1+up
            elif prev==cur:
                up, down, peak = 0, 0, 0
                res += 1
            else:
                up, down = 0, 1+down
                res += 1+down-int(peak>=down)    
        return res