import random
from queue import Queue


class BFS:
    def __init__(self, adj_lis):
        self.adj_lis = adj_lis
        self.visited = {}
        self.level = {}
        self.parent = {}

        for n in self.adj_lis:
            self.visited[n] = False
            self.level[n] = -1
            self.parent[n] = None

    def graph(self, s=None, e=None):
        q = Queue()
        if s is None:
            s = random.choice([i for i in self.adj_lis.keys()])
        q.put(s)
        self.visited[s] = True
        self.level[s] = 0

        res = []

        while not q.empty():
            u = q.get()
            if e and u == e:
                res.append(u)
                break

            res.append(u)
            for v in self.adj_lis[u]:
                if not self.visited[v]:
                    self.level[v] = self.level[u] + 1
                    self.parent[v] = u
                    self.visited[v] = True
                    q.put(v)
        return res

    def get_shortest_path(self, v):
        path = []
        while v is not None:
            path.append(v)
            v = self.parent[v]
        return path

    def get_distance(self, s, e):
        return abs(self.level[s] - self.level[e])


adj_list = {
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['B'],
    'D': ['A', 'E', 'F'],
    'E': ['D', 'F', 'G'],
    'F': ['D', 'E', 'H'],
    'G': ['E', 'H'],
    'H': ['G', 'F']
}

graph = BFS(adj_list)
print(graph.graph("A", "G"))
