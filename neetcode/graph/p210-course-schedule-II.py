# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

# Example 2:
# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

# Example 3:
# Input: numCourses = 1, prerequisites = []
# Output: [0]

# Recursive DFS and Topological Sort (not uquique, no cycle) Solution |
# Complexity: O(v+e) Time | O(v+e) Space
# v -> The number of vertices in the graph | e -> The number of edges in the graph
## a course has three possible states:
## visited --> course has been added to output
## visiting --> crs not added to output, but added to cycle
## unvisited --> crs not added to output or cycle

from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #build adjancency list of prereqs
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
                
        visit, cycle = set(), set()
        output= []
        
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True    #not stop algorithm, but crs is visited     
            
            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:  #cycle detected
                    return False

            cycle.remove(crs)          # no longer along the path we are going
            visit.add(crs)             
            output.append(crs)         # visited with prereqs, so add to output
            return True

        for c in range(numCourses):
            if dfs(c) == False:        #cycle detected
                return []
        return output  
            
        