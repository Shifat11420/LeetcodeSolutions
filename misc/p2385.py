# You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.
# Each minute, a node becomes infected if:
# The node is currently uninfected.
# The node is adjacent to an infected node.
# Return the number of minutes needed for the entire tree to be infected.

# Example 1:
# Input: root = [1,5,3,null,4,10,6,9,2], start = 3
# Output: 4
# Explanation: The following nodes are infected during:
# - Minute 0: Node 3
# - Minute 1: Nodes 1, 10 and 6
# - Minute 2: Node 5
# - Minute 3: Node 4
# - Minute 4: Nodes 9 and 2
# It takes 4 minutes for the whole tree to be infected so we return 4.

# Example 2:
# Input: root = [1], start = 1
# Output: 0
# Explanation: At minute 0, the only node in the tree is infected so we return 0.
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        if not root:
            return 0

        startnode = [None]
        par = {}
        def dfs(node):
            if node:
                if node.val == start:
                    startnode[0] = node
                if node.left:
                    par[node.left] = node
                    dfs(node.left)
                if node.right:
                    par[node.right] = node           
                    dfs(node.right)

        dfs(root)

        visit = set()
        visit.add(startnode[0].val)
        q = deque([startnode[0]])
        time = -1
        
        while q:
     
            for i in range(len(q)):
                node = q.popleft()
                if node in par and par[node].val not in visit:
                    q.append(par[node])
                    visit.add(par[node].val)
                if node.left and node.left.val not in visit:
                    q.append(node.left)
                    visit.add(node.left.val)
                if node.right and node.right.val not in visit:
                    q.append(node.right)
                    visit.add(node.right.val)
            time += 1                
        return time            
        
# efficient approach
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def dfs(node):
            if node is None:
                return
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
            dfs(node.left)
            dfs(node.right)

        graph = defaultdict(list)
        dfs(root)
        visited = set()
        queue = deque([start])
        time = -1
        while queue:
            time += 1
            for _ in range(len(queue)):
                current_node = queue.popleft()
                visited.add(current_node)
                for neighbor in graph[current_node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return time        