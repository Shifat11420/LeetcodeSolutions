
# https://leetcode.com/problems/clone-graph/
# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
 

# Test case format:

# For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

# An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

# The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

# Here and below, V and E refer to the number of vertices and edges in a graph G = (V, E), respectively.

# Time complexity: O(V + E), because we need to visit all vertices and traverse all edges in the graph.
# Space complexity: O(V), because the worst case is when we have a complete graph (i.e. there's an edge between every pair of vertices), in which the depth of the recursion stack would be the number of nodes in the graph.
# To construct the clone graph, we need to traverse through the original graph and generate the copy nodes at the same time. To allow us to be able to form the edge connections properly, we need a mapping that lets us know what the original edge connections/relationships were in the original graph. Hence why we're using a map to map nodes in the original graph to nodes in the copy graph. Since the graph is undirected, whenever there's an edge from A -> B, there's also one from B -> A. Thus, to not get caught in an infinite loop, the visited map serves the dual purpose of allowing us to keep track of which nodes we've already visited, so that we don't visit them yet again.


#Recursive DFS solution using built-in stack
"""
Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: 'Node')-> 'Node':
        if node == None:
            return node
        visited = {}
        
        def dfs(node):
            if node in visited:
                return visited[node]
            
            clone = Node(node.val)
            visited[node] = clone
            
            for neighbor in node.neighbors:
                visited[node].neighbors.append(dfs(neighbor))
                
            return clone
        return dfs(node)    
