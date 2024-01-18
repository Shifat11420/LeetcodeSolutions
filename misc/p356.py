# Given n points on a 2D plane, find if there is such a line parallel to the y-axis that reflects the given points symmetrically.
# In other words, answer whether or not if there exists a line that after reflecting all points over the given line, the original points' set is the same as the reflected ones.
# Note that there can be repeated points.

# Example 1:
# Input: points = [[1,1],[-1,1]]
# Output: true
# Explanation: We can choose the line x = 0.

# Example 2:
# Input: points = [[1,1],[-1,-1]]
# Output: false
# Explanation: We can't choose a line.

# # Time: O(n+nlogn), Space: O(n)
# class Solution:
#     def isReflected(self, points: List[List[int]]) -> bool:
#         if len(points) == 1:
#             return True
        
#         hm = defaultdict(list)
#         for x,y in points:
#             hm[y].append(x)

#         l =list(hm.values())[0]          
#         l = list(set(l))
  
#         if len(l)%2:
#             l.sort()
#             left, right = 0, len(l)-1
#             k =(l[left]+l[right])/2
#             while left<=right:
#                 if (left==right and l[left]!=k) or (l[left]+l[right])/2!=k:
#                     return False
#                 left+=1
#                 right-=1    
#         v = sum(l)/len(l)

#         for l in hm.values():
#             l = list(set(l))   
#             m = sum(l)/len(l)       
#             if v != m:
#                 return False
#         return True         

# Time: O(n), Space: O(n)
class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        xpoints = [x for x,y in points]
        minx = min(xpoints)
        maxx = max(xpoints)
        center = (minx+maxx)/2

        hashset = set()
        for x,y in points:
            hashset.add((x,y))

        for x,y in points:
            if (2*center-x, y) not in hashset:
                return False
        return True             