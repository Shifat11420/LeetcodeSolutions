# Suppose you are at a party with n people labeled from 0 to n - 1 and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know the celebrity, but the celebrity does not know any of them.
# Now you want to find out who the celebrity is or verify that there is not one. You are only allowed to ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).
# You are given a helper function bool knows(a, b) that tells you whether a knows b. Implement a function int findCelebrity(n). There will be exactly one celebrity if they are at the party.
# Return the celebrity's label if there is a celebrity at the party. If there is no celebrity, return -1.

# Example 1:
# Input: graph = [[1,1,0],[0,1,0],[1,1,1]]
# Output: 1
# Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.

# Example 2:
# Input: graph = [[1,0,1],[1,1,0],[0,1,1]]
# Output: -1
# Explanation: There is no celebrity.
 # The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    # brute force, time limit exceeded
    # def findCelebrity(self, n: int) -> int:
    #     count=[{"in":0, "out":0} for _ in range(n)]
    #     for i in range(n):
    #         for j in range(n):
    #             if i != j: 
    #                 if knows(i, j)==1:
    #                     count[i]["out"]+=1
    #                     count[j]["in"]+=1

    #     for i in range(n):                 
    #         if count[i]["in"] == n-1 and count[i]["out"]==0:
    #             return i
    #     return -1     

    # Time : O(n), space O(n)
    def findCelebrity(self, n: int) -> int:
        # reduce calls to know
        cache = {}
        def knows_cache(i,j):
            if (i,j) not in cache:
                cache[(i,j)]=knows(i,j)
            return cache[(i,j)]

        # set an initial candidate so we only have to loop through once
        candidate = 0
        for c in range(1, n):
            if knows_cache(candidate,c):
                candidate = c

        # verify that our candidate is the celebrity
        for i in range(n):
            if i != candidate:
                if not knows_cache(i,candidate) or knows_cache(candidate,i):
                    return -1
        return candidate                    
