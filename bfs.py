#BFS---Queue (FIFO) based

class Graph:
    def __init__(self):
        self.list = {}

    def createEdge(self, start, end):
        if start in self.list.keys():
            self.list[start].append(end)
        else:
            self.list[start] = [end]

    def display(self):
        for i in self.list:
            print(i, ':', [j for j in self.list[i]])

    def bfs(self, startnode):
        visited = [False] * (max(self.list)+1)
        queue = []

        visited[startnode] = True
        queue.append(startnode)

        while queue:
            startnode = queue.pop(0)
            print(startnode, end=' ')

            for i in self.list[startnode]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True       



if __name__ == '__main__':
    g = Graph()
    # g.createEdge(0,1)
    # g.createEdge(0,2)
    # g.createEdge(1,2)
    # g.createEdge(2,0)
    # g.createEdge(2,3)
    # g.createEdge(3,3)
 

  
    # g.createEdge(1,2)
    # g.createEdge(1,3)
    # g.createEdge(2,4)
    # g.createEdge(2,5)
    # g.createEdge(3,5)
    # g.createEdge(4,5)
    # g.createEdge(4,6)
    # g.createEdge(5,6)


    g.createEdge(0, 1)
    g.createEdge(0, 2)
    g.createEdge(1, 2)
    g.createEdge(2, 0)
    g.createEdge(2, 3)
    g.createEdge(3, 3)

    # g.createEdge('A', 'B')
    # g.createEdge('A', 'C')
    # g.createEdge('A', 'D')
    # g.createEdge('B', 'E')
    # g.createEdge('B', 'F')
    # g.createEdge('C', 'G')
    # g.createEdge('D', 'H')

    g.display()
    g.bfs(0)
# https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/