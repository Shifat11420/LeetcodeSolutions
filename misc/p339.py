# You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.
# The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.
# Return the sum of each integer in nestedList multiplied by its depth. 

# Example 1:
# Input: nestedList = [[1,1],2,[1,1]]
# Output: 10
# Explanation: Four 1's at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.

# Example 2:
# Input: nestedList = [1,[4,[6]]]
# Output: 27
# Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3. 1*1 + 4*2 + 6*3 = 27.

# Example 3:
# Input: nestedList = [0]
# Output: 0
 
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

# Time : O(n), Space: O(n)
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        res = 0
        stack, flag, s = [], False, 0
        nl = str(nestedList)
        for i,c in enumerate(nl):
            if c=="[":
                if not stack:
                    count = 1
                else:
                    count = stack[-1][1]+1    
                stack.append([c, count])
            elif c=="]":
                stack.pop()
            elif c== "-":
                flag = True
            elif c.isdigit():
                s = s*10+int(c)
                if nl[i+1].isdigit():
                    continue 
                cursum = int(s)*stack[-1][1]
                res = res-cursum if flag else res+cursum 
                flag = False
                s = 0
            else:
                continue               
        return res 

# Time : O(n), Space: O(1)
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def helper(nestedList, depth):
            total = 0
            for item in nestedList:
                if item.isInteger():
                    total += item.getInteger()*depth
                elif item.getList():
                    total += helper(item.getList(), depth+1)
            return total            

        sum = helper(nestedList, depth = 1)
        return sum    