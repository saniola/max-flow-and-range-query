import matplotlib.pyplot as plt
import networkx as nx

def draw_flow_network(graph):
  G = nx.DiGraph()

  for u in graph.flow_graph:
    for v, flow in graph.flow_graph[u].items():
        if flow > 0:
            G.add_edge(u, v, weight=flow)

  pos = nx.spring_layout(G)
  plt.figure(figsize=(12, 8))

  nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightblue')
  nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=15, edge_color='gray')
  nx.draw_networkx_labels(G, pos, font_size=10, font_color='black')

  edge_labels = {(u, v): f"{d['weight']}" for u, v, d in G.edges(data=True)}
  nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9)

  plt.title("Граф фактичного потоку логістичної мережі")
  plt.show()
