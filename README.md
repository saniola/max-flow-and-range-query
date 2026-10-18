# Max Flow and Range Query

Two independent Python algorithm demonstrations: maximum flow in a logistics network and range-query performance comparison between a B-tree and a dictionary.

## Contents

### `task1/` — Maximum Flow (Edmonds-Karp)

Models a two-terminal, four-warehouse, fourteen-store logistics network as a flow graph and computes the maximum flow from each terminal to each store using the Edmonds-Karp algorithm (BFS-based Ford-Fulkerson).

- `max_flow.py` — `MaxFlow` class implementing the graph and the Edmonds-Karp algorithm.
- `main.py` — builds the network, computes flows for every terminal/store pair, and prints a results table.
- `graph.py` — draws the flow network.
- `analysis.py` — analyzes and summarizes the computed flow results.

Run from the repository root:

```bash
python -m task1.main
```

### `task2/` — B-Tree vs. Dictionary Range Queries

Loads ~100,000 generated product records from `generated_items_data.csv` into both an `OOBTree` (from the `BTrees` package) and a plain Python dictionary, then benchmarks range queries by price on each structure using `timeit`.

Run from the repository root:

```bash
python task2/main.py
```

## Stack

- Python 3
- `pandas`, `matplotlib` (task1)
- `BTrees` (task2)

## Usage

```bash
pip install pandas matplotlib BTrees
python -m task1.main
python task2/main.py
```
