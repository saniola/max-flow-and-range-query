from collections import deque, defaultdict


class MaxFlow:
  def __init__(self, vertices):
    self.vertices = vertices
    self.graph = defaultdict(dict)
    self.flow_graph = defaultdict(lambda: defaultdict(int))

  def add_edge(self, u, v, capacity):
    self.graph[u][v] = capacity
    self.graph[v].setdefault(u, 0)

  def bfs(self, source, sink, parent):
    visited = set()
    queue = deque([source])
    visited.add(source)

    while queue:
      u = queue.popleft()
      for v, capacity in self.graph[u].items():
        if v not in visited and capacity > 0:
          queue.append(v)
          visited.add(v)
          parent[v] = u
          if v == sink:
            return True
    return False

  def edmonds_karp(self, source, sink):
    parent = {}
    max_flow = 0

    while self.bfs(source, sink, parent):
      path_flow = float('Inf')
      s = sink
      while s != source:
        path_flow = min(path_flow, self.graph[parent[s]][s])
        s = parent[s]

      v = sink
      while v != source:
        u = parent[v]
        self.graph[u][v] -= path_flow
        self.graph[v][u] += path_flow
        self.flow_graph[u][v] += path_flow
        v = parent[v]

      max_flow += path_flow

    return max_flow
