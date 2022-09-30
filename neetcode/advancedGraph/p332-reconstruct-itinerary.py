# You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.
# All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.
# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

# Example 1:
# Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# Output: ["JFK","MUC","LHR","SFO","SJC"]

# Example 2:
# Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.

# sort adjacency listfor lexical order---> sort input
# len(res) = len(tickets) + 1 (1 for starting node)
# DFS, backtracking
# Complexity: time O(v+e)^2--> O(e^2), space O(e)

from typing import List
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src:[] for src, dst in tickets}
        
        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)
        
        res = ["JFK"]
        def dfs(src):
            if len(res)==len(tickets)+1:
                return True
            if src not in adj:
                return False
            
            temp = list(adj[src])         # making a copy since you cannot change and iterate through a list at the same time
            for i, v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)
                if dfs(v):
                    return True
                adj[src].insert(i,v)     # if dfs(v) not true, you have to go backwords     
                res.pop()
        dfs("JFK")
        return res