# You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.
# If node i has no left child then leftChild[i] will equal -1, similarly for the right child.
# Note that the nodes have no values and that we only use the node numbers in this problem.

# Example 1:
# Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
# Output: true

# Example 2:
# Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
# Output: false

# Example 3:
# Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
# Output: false
 
# Time: O(n), Space: O(n)
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        childCount = [False]*n
        for i in leftChild:
            if i!=-1:
                childCount[i] = True
        for i in rightChild:
            if i!=-1:
                if childCount[i]:
                    return False
                childCount[i] = True

        root = -1
        for i in range(n):
            if not childCount[i]:
                if root==-1:
                    root = i
                else: 
                    return False
        if root==-1:
            return False
        visit = [False]*n
        visit[root] = True    
        if not self.checkTree(root, leftChild, rightChild, visit):
            return False
        for v in visit:
            if not v:
                return False
        return True                                            

    def checkTree(self, cur, leftChild, rightChild, visit):
        if leftChild[cur] != -1:
            if visit[leftChild[cur]]:
                return False
            visit[leftChild[cur]] = True

            if not self.checkTree(leftChild[cur], leftChild, rightChild, visit):
                return False

        if rightChild[cur] != -1:
            if visit[rightChild[cur]]:
                return False
            visit[rightChild[cur]] = True        

            if not self.checkTree(rightChild[cur], leftChild, rightChild, visit):
                return False
        return True    