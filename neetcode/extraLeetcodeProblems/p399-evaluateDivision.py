# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
# Return the answers to all queries. If a single answer cannot be determined, return -1.0.
# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

# Example 1:
# Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
# Explanation:
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]

# Example 2:
# Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# Output: [3.75000,0.40000,5.00000,0.20000]

# Example 3:
# Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
# Output: [0.50000,2.00000,-1.00000,-1.00000]

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Step 1. Build the Graph
        graph = collections.defaultdict(dict)

        for (x, y), val in zip(equations, values):
            graph[x][y] = val
            graph[y][x] = 1.0/val

        # Step 2. DFS function
        def dfs(x, y, visit):
            # neither x not y exists
            if x not in graph or y not in graph:
                return -1.0

            # x points to y
            if y in graph[x]:
                return graph[x][y]

            # x maybe connected to y through other nodes
            # use dfs to see if there is a path from x to y
            for i in graph[x]:
                if i not in visit:
                    visit.add(i)
                    temp = dfs(i, y, visit)
                    if temp == -1.0:
                        continue
                    else:
                        return graph[x][i]*temp
            return -1

        res = []
        for qpair in queries:
            x, y = qpair
            res.append(dfs(x, y, set()))
        return res
