def analyze_results(graph, df_results):
  total_flow_by_terminal = df_results.groupby("Термінал")["Фактичний Потік (одиниць)"].sum()
  print("Термінали з найбільшим потоком:")
  print(total_flow_by_terminal.sort_values(ascending=False))

  print("\nМаршрути з найменшою пропускною здатністю:")
  for u in graph.graph:
    for v, capacity in graph.graph[u].items():
      if capacity == 0:
        print(f"Ребро {u} -> {v} є вузьким місцем")

  total_flow_by_shop = df_results.groupby("Магазин")["Фактичний Потік (одиниць)"].sum()
  print("\nМагазини з найменшим потоком:")
  print(total_flow_by_shop.sort_values())

  print("\nВузькі місця та рекомендації щодо покращення:")
  for u in graph.graph:
    for v, capacity in graph.graph[u].items():
      if capacity == 0:
        print(f"Рекомендується збільшити пропускну здатність ребра {u} -> {v}")
