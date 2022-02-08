
# https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/ 
# Given an array arr of positive integers, consider all binary trees such that:

# Each node has either 0 or 2 children;
# The values of arr correspond to the values of each leaf in an in-order traversal of the tree.
# The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree, respectively.
# Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node. It is guaranteed this sum fits into a 32-bit integer.

# A node is a leaf if and only if it has zero children.


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        
        ans = 0
        
        while len(arr)>1:
            minindex = arr.index(min(arr))
            if 0< minindex < len(arr)-1:
                ans += min(arr[minindex-1], arr[minindex+1]) * arr[minindex]   
            else:                                #handle corner cases
                ans += arr[1 if minindex == 0 else minindex-1] * arr[minindex]
            print(ans)    
            arr.pop(minindex)     
        return ans     