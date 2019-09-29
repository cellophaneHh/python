'''
bfs
'''
import random


class BFS:
    def __init__(self):
        self.__root = 0
        self.init(6)
        self.__edgeTo = [False, False, False, False, False, False]
        self.__marked = [False, False, False, False, False, False]

    def init(self, n):
        self.__graph = [
            [2, 1, 5],
            [0, 3],
            [0, 4],
            [1, 5, 4],
            [2, 3],
            [0, 3],
        ]

    def graph(self):
        return self.__graph

    def adj(self, m):
        return graph[m]

    def __bfs(self, v, m):
        for p in self.adj(v):
            if not self.__marked[p]:
                self.__marked[p] = True
                self.__edgeTo[p] = v
                self.__bfs(p, m)

    def pathTo(self, v, m):
        self.__marked[self.__root] = True
        self.__bfs(self.__root, m)
        print(self.__edgeTo)
        n = self.__edgeTo[m]
        path = []
        while n != v:
            path.insert(0, n)
            n = self.__edgeTo[n]
        path.insert(0, v)
        return path


bfs = BFS()
print()
graph = bfs.graph()
path = bfs.pathTo(0, 4)
print(path)
