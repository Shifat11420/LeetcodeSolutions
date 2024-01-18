# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.
# Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

# Example 1:
# Input: path = "NES"
# Output: false 
# Explanation: Notice that the path doesn't cross any point more than once.

# Example 2:
# Input: path = "NESWW"
# Output: true
# Explanation: Notice that the path visits the origin twice.

#Time : O(n), Space: O(n)
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visit = set()
        dir = { "N": [-1,0],
                "S": [1,0],
                "W": [0,-1],
                "E": [0,1]
                }
        r, c = 0, 0
        visit.add((r,c))
        for s in path:
            dr,dc = dir[s]
            r , c = r+dr, c+dc
            if (r,c) in visit:
                return True
            visit.add((r,c))
        return False        

        