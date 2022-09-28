# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

# Example 1:
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2

# Example 2:
# Input: times = [[1,2,1]], n = 2, k = 1
# Output: 1

# Example 3:
# Input: times = [[1,2,1]], n = 2, k = 2
# Output: -1

# Djikstra's, BFS (Djkstra's  algo is a BFS with minHeap)
#  E = no. of edges, v= no of vertices, E = v^2 (max size of heap, bidirectional edges, nodes added to the heap multiple times)
# Complexity: O(E*log(V^2)) (every heap operation worse case logV^2, how many times? E = no of edges times)----> O(2E*logV)----> O(E*logV)
import collections
import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # create adjacency list
        edges = collections.defaultdict(list)  # empty list, hashmap
        for u, v, w in times:
            edges[u].append((v, w))
        
        #djikstra's
        visit = set()
        t = 0
        minHeap = [(0, k)]     #[weight, node]
        while minHeap:
            weight, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            t = max(t, weight)
            for v2, w2 in edges[node]:
                if v2 not in visit:
                    heapq.heappush(minHeap, (weight+ w2, v2))
                    
        return t if len(visit) == n else -1        
                    