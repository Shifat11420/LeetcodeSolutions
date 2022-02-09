# https://leetcode.com/problems/operations-on-tree/submissions/ 
#You are given a tree with n nodes numbered from 0 to n - 1 in the form of a parent array parent where parent[i] is the parent of the ith node. The root of the tree is node 0, so parent[0] = -1 since it has no parent. You want to design a data structure that allows users to lock, unlock, and upgrade nodes in the tree.

from collections import defaultdict, deque


class LockingTree:
    
    def __init__(self, parent: List[int]):
        self.graph = defaultdict(dict)
        for u, v in enumerate(parent):
            self.graph[v][u] = 1
        self.locked = defaultdict(int)
        self.parent = parent

    def lock(self, num: int, user: int) -> bool:
        if self.locked[num] != 0:
            return False                   #already locked
        self.locked[num] = user
        return True     

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] == user:
            self.locked[num] = 0
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
      
        def has_locked_ancestors(node):
            if node == -1:
                return False
            if self.locked[node] > 0:
                return True                  
            return has_locked_ancestors(self.parent[node])
        
        def unlock_descendants(node):
            q = deque([node])
            visited = set()
            visited.add(node)
            count = 0
            
            while q:
                u = q.popleft()
                for v in self.graph[u]:
                    if self.locked[v] != 0:
                        count += 1
                        self.locked[v] = 0
                    if v not in visited:
                        visited.add(v)
                        q.append(v)
            return count>0
            
    
        if self.locked[num] == 0 and  has_locked_ancestors(self.parent[num]) is False and unlock_descendants(num):
            self.locked[num] = user
            return True 
        return False


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)