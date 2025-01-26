from task1.graph import draw_flow_network
from task1.analysis import analyze_results
import pandas as pd
from task1.max_flow import MaxFlow

graph = MaxFlow(20)

connections = [
  ("T1", "S1", 25), ("T1", "S2", 20), ("T1", "S3", 15),
  ("T2", "S3", 15), ("T2", "S4", 30), ("T2", "S2", 10),
  ("S1", "M1", 15), ("S1", "M2", 10), ("S1", "M3", 20),
  ("S2", "M4", 15), ("S2", "M5", 10), ("S2", "M6", 25),
  ("S3", "M7", 20), ("S3", "M8", 15), ("S3", "M9", 10),
  ("S4", "M10", 20), ("S4", "M11", 10), ("S4", "M12", 15),
  ("S4", "M13", 5), ("S4", "M14", 10)
]

for u, v, capacity in connections:
  graph.add_edge(u, v, capacity)

sources = ["T1", "T2"]
sinks = ["M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9", "M10", "M11", "M12", "M13", "M14"]

results = []
for source in sources:
  for sink in sinks:
    max_flow = graph.edmonds_karp(source, sink)
    results.append({"Термінал": source, "Магазин": sink, "Фактичний Потік (одиниць)": max_flow})

df_results = pd.DataFrame(results)

print(df_results)
analyze_results(graph, df_results)
draw_flow_network(graph)