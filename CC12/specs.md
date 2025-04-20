## Coding Challenge 12: Shortest Path Algorithms



---

<img src="img/Google1.png" alt="AI" width="400"/>




## Problem 1: Dijkstra's Algorithm (Shortest Path in Directed Graph)

You are given an integer `start` and a list `edges` that defines a directed graph in the form of an **adjacency list**. Each index `i` in `edges` contains a list of `i`'s outgoing edges, each represented by a pair:

```python
[destination, distance]
```

- `destination`: a vertex index
- `distance`: a positive integer weight of the edge from vertex `i` to `destination`

Write a function that calculates the **shortest distance** from the start vertex to all other vertices using **Dijkstra’s algorithm**.

Return a list `output` where `output[i]` is the shortest distance from `start` to vertex `i`, or `-1` if vertex `i` is unreachable.

### Constraints
- No self-loops
- Only positive edge weights
- Directed graph

---

### Input
```python
start = 0
edges = [
  [[1, 7]],
  [[2, 6], [3, 20], [4, 3]],
  [[3, 14]],
  [[4, 21]],
  [],
  [],
]
```

### Output
```python
[0, 7, 13, 27, 10, -1]
```

---

### Time & Space Complexity
- **Time:** O((v + e) * log v)
- **Space:** O(v)

Where \(v\) is the number of vertices, and \(e\) is the number of edges.

---


<img src="img/Techno.png" alt="ML" width="400"/>

## Problem 2: A* Search Algorithm (Shortest Path in Grid)

You're given a grid (2D list) of `0`s and `1`s, where `0` indicates a free space and `1` indicates an obstacle. Four integers `start_row`, `start_col`, `end_row`, and `end_col` are also provided to specify the start and end coordinates within the grid.

Write a function that uses the **A\*** algorithm to find and return the shortest path from the start to the end as a list of coordinate pairs. Each step in the returned list should be a list: `[row, col]`. The output path must begin with the start node and end with the destination node.

Return an **empty list** if there is no path.

### Notes
- Only 4-directional movement is allowed: up, down, left, right
- All moves have equal cost
- The start and end positions will always be in free cells (`0`) and will never be out of bounds
- At most one shortest path exists between the start and end

---

### Sample Input
```python
start_row = 0
start_col = 1
end_row = 4
end_col = 3
graph = [
  [0, 0, 0, 0],
  [0, 1, 1, 0],
  [0, 0, 0, 0],
  [1, 0, 1, 1],
  [0, 0, 0, 0],
]
```

### Sample Output
```python
[[0, 1], [0, 0], [1, 0], [2, 0], [2, 1], [3, 1], [4, 1], [4, 2], [4, 3]]
```

---

### Time & Space Complexity
- **Time:** O(w * h * log(w * h))
- **Space:** O(w * h)

Where \(w\) is the width and \(h\) is the height of the grid.

> These problems emphasize different applications of shortest-path search: Dijkstra's on graphs with varying weights, and A* on grid-based maps with obstacles.

