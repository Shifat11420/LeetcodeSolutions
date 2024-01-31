# You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).
# There is at least one empty seat, and at least one person sitting.
# Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 
# Return that maximum distance to the closest person. 

# Example 1:
# Input: seats = [1,0,0,0,1,0,1]
# Output: 2
# Explanation: 
# If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
# If Alex sits in any other open seat, the closest person has distance 1.
# Thus, the maximum distance to the closest person is 2.

# Example 2:
# Input: seats = [1,0,0,0]
# Output: 3
# Explanation: 
# If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
# This is the maximum distance possible, so the answer is 3.

# Example 3:
# Input: seats = [0,1]
# Output: 1

# Time: O(n), Space: O(1)
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        left = seats.index(1)
        seats.reverse()
        right = seats.index(1)

        maxlen = 0
        for seat, group in itertools.groupby(seats):
            if not seat:
                K = len(list(group))
                maxlen = max(maxlen, K)    

        # maxlen = 0
        # i = 0
        # while i<len(seats):
        #     length = 0
        #     if seats[i]==0:
        #         while i<len(seats) and seats[i]==0:
        #             length += 1
        #             i += 1
        #         maxlen = max(maxlen, length)    
        #     else:
        #         i+=1

        mid = (maxlen+1)//2

        return max(left, mid, right)    