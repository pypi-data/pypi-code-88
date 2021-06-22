from collections import deque
import numpy as np


def search(adj_matrix, birth):
    return Finder(adj_matrix, birth).search()

TERM = -1

class Finder(object):
    def __init__(self, adjacent_matrix, birth):
        self.matrix = adjacent_matrix
        self.birth = birth
        self.visited = set()
        self.prev = dict()

    def search(self):
        start, end = self.search_starting_edge()
        g = self.matrix < self.birth
        queue = deque([start])
        self.visited.add(start)
        self.prev[start] = TERM
        
        while queue:
            v = queue.popleft()
            if v == end:
                return self.path(end)
            for n in range(self.num_points):
                if not g[n, v]:
                    continue
                if n in self.visited:
                    continue
                
                self.visited.add(n)
                self.prev[n] = v
                queue.append(n)

        raise(RuntimeError("No loop containing birth"))

    def path(self, end):
        v = end
        path = []
        while True:
            path.append(v)
            v = self.prev[v]
            if v == TERM:
                return path

    def search_starting_edge(self):
        xs, ys = np.nonzero(self.matrix == self.birth)
        if xs.size == 0:
            raise(RuntimeError("Invalid birth time"))
        if xs.size > 2:
            raise(RuntimeError("Pairs with the same birth time"))
        return sorted([xs[0], ys[0]])

    @property
    def num_points(self):
        return self.matrix.shape[0]

        
    
