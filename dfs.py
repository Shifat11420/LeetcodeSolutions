#DFS---Stack (LIFO) based

# class Graph:
#     def __init__(self):
#         self.list = {}

#     def createEdge(self, start, end):
#         if start in self.list.keys():
#             self.list[start].append(end)
#         else:
#             self.list[start] = [end]

#     def display(self):
#         for i in self.list:
#             print(i, ':', [j for j in self.list[i]])        

#     def dfs(self, startnode):
#         visited = [False] * (max(self.list)+1)    
#         stackk = []

#         visited[startnode] = True
#         stackk.append(startnode)

#         while stackk:
#             startnode = stackk.pop(len(stackk)-1)
#             print(startnode, end=' ')

#             for i in  self.list[startnode]:
#                 if visited[i] == False:
#                     stackk.append(i)
#                     visited[i] = True
                
#                 visited[startnode] = True

# if __name__== '__main__':
#     g = Graph()
#     # g.createEdge(0, 1)
#     # g.createEdge(0, 2)
#     # g.createEdge(1, 2)
#     # g.createEdge(2, 0)
#     # g.createEdge(2, 3)
#     # g.createEdge(3, 3)

#     g.createEdge(0, 1)
#     g.createEdge(0, 2)
#     g.createEdge(1, 2)
#     g.createEdge(2, 0)
#     g.createEdge(2, 3)
#     g.createEdge(3, 3)

#     g.display()
#     g.dfs(0)


from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, start, end):
        self.graph[start].append(end)

    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v)

        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.DFSUtil(neighbor, visited)

    def DFS(self):
        visited = set()

        for vertex in self.graph:
            if vertex not in visited:
                self.DFSUtil(vertex, visited)

if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    g.DFS()           

# https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/