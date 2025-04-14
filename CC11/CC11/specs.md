## 🧠 Coding Challenge

This challenge consists of two problems designed to test your understanding of recursion, traversal, and indexing logic.

---

## 🔢 Problem 1: Depth-First Search

You are provided with a `Node` class that includes a `name` attribute and a list of optional `children` nodes. These nodes together form a tree-like, acyclic structure.

Your task is to implement the `depth_first_search` method within the `Node` class. This method should take an initially empty list, traverse the tree using the **depth-first search (DFS)** strategy — visiting child nodes from **left to right** — and append each node's name to the list in the order visited. The method should return the updated list.

### 🔍 Function Signature

```python
def depth_first_search(self, array: List[str]) -> List[str]:
    # your code here
```

---

### ✅ Example 1 

#### Tree Structure

```
        A
      / | \
     B  C  D
    / \    / \
   E   F  G   H
      / \      \
     I   J      K
```

#### Code

```python
graph = Node("A")
graph.children = [Node("B"), Node("C"), Node("D")]
graph.children[0].children = [Node("E"), Node("F")]
graph.children[0].children[1].children = [Node("I"), Node("J")]
graph.children[2].children = [Node("G"), Node("H")]
graph.children[2].children[0].children = [Node("K")]
```

#### Expected Output

```python
["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]
```

---

### ✅ Example 2

#### Tree Structure

```
      X
     / \
    Y   Z
   / \
  P   Q
```

#### Code

```python
graph = Node("X")
graph.children = [Node("Y"), Node("Z")]
graph.children[0].children = [Node("P"), Node("Q")]
```

#### Expected Output

```python
["X", "Y", "P", "Q", "Z"]
```

---

### ✅ Example 3

#### Tree Structure

```
     M
    /
   N
  / \
 O   P
     |
     Q
```

#### Code

```python
graph = Node("M")
graph.children = [Node("N")]
graph.children[0].children = [Node("O"), Node("P")]
graph.children[0].children[1].children = [Node("Q")]
```

#### Expected Output

```python
["M", "N", "O", "P", "Q"]
```

---

### ✅ Example 4

#### Tree Structure

```
      R
    / | \
   S  T  U
      |
      V
     / \
    W   X
```

#### Code

```python
graph = Node("R")
graph.children = [Node("S"), Node("T"), Node("U")]
graph.children[1].children = [Node("V")]
graph.children[1].children[0].children = [Node("W"), Node("X")]
```

#### Expected Output

```python
["R", "S", "T", "V", "W", "X", "U"]
```

---

### 🧮 Optimal Space & Time Complexity

- **Time Complexity:** `O(v + e)`
- **Space Complexity:** `O(v)`\
  Where `v` is the number of nodes (vertices) in the input tree and `e` is the number of edges.

---


### 🔍 Visual Resource: Understanding Graph Traversals  

To support your implementation and deepen your intuition for graph algorithms, please explore this interactive visualization tool. It allows you to step through the logic of **Depth-First Search (DFS)** and **Breadth-First Search (BFS)** on a sample graph or your own custom input.

🔗 **[VisuAlgo – DFS & BFS Visualizations](https://visualgo.net/en/dfsbfs)**  
(*Source: VisuAlgo – Free for educational use*)

📌 *Use this tool to visualize traversal orders, queue/stack behavior, and node exploration patterns. Helpful before or after coding your solution.*




## 🔄 Problem 2: Single Cycle Check

You're given an array of integers where each integer represents a jump of its value in the array. For instance, the integer `2` represents a jump of two indices forward in the array; the integer `-3` represents a jump of three indices backward in the array.

If a jump spills past the array's bounds, it wraps over to the other side. For example, a jump of `-1` at index `0` brings you to the last index. Similarly, a jump of `1` at the last index in the array brings you to index `0`.

Write a function that returns a boolean representing whether the jumps in the array form a **single cycle**. A single cycle occurs if, starting at any index in the array and following the jumps, every element in the array is visited exactly once before landing back on the starting index.

### 🔍 Function Signature

```python
def has_single_cycle(array: List[int]) -> bool:
    # your code here
```

### 📥 Sample Input

```python
array = [2, 3, 1, -4, -4, 2]
```

### 📤 Sample Output

```python
True
```

### 💡 Hints

- **Hint 1:** Use a counter to track how many elements you've jumped through. You can stop when you've visited `n` elements.
- **Hint 2:** Consider what conditions break the cycle if the array length is `n`. You must end exactly where you started.
- **Hint 3:** Two key checks: (1) No element (other than index 0) should be visited more than once before visiting all elements. (2) The last element must bring you back to index 0.

---

### 🧮 Optimal Space & Time Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`\
  Where `n` is the length of the input array.

---




