# Project 5: AVL Trees

**Due: April 4th , 2024 @ 9:00 PM EST**

_This is not a team project. Do not copy someone else’s work._

## Assignment Overview

> We must find balance...

![THANOS](img/thanos.jpg)

[AVL trees](https://en.wikipedia.org/wiki/AVL_tree), named after computer scientists Georgy Adelson-Velsky and Evgenii Landis, who introduced them in 1962, are a type of self-balancing [binary search tree (BST)](https://en.wikipedia.org/wiki/Binary_search_tree) designed to maintain operations in logarithmic time, regardless of data insertion and deletion patterns. Their introductory paper, "[An Algorithm for the Organization of Information](https://zhjwpku.com/assets/pdf/AED2-10-avl-paper.pdf)," stands as a testament to their enduring relevance, especially in applications requiring a space-efficient data structure with quick insertion, search, and deletion capabilities.

![AVL Tree Animation](img/avl.gif)

A critical issue often encountered with traditional BSTs is their tendency to become _unbalanced_ depending on the order of data insertion and deletion, leading to operations taking linear time instead of logarithmic. For instance, inserting data in a sorted (or reverse-sorted) sequence results in a BST that resembles a linked list, with leaves growing predominantly in one direction.

![BST Balancing Issue](img/balance.png)

While this may not pose significant challenges with small datasets, the performance gap between logarithmic and linear time becomes dramatically evident when dealing with large databases comprising thousands or millions of records.

![Logarithmic vs. Linear Growth](img/bigogrowth.png)

By self-balancing, AVL trees ensure that operations consistently take logarithmic time, providing a robust solution to the issues faced by traditional BSTs. In this project, you are tasked with implementing both a traditional BST and an AVL tree from the ground up in Python. Utilizing the AVL tree, you will address a machine-learning-inspired application problem.

## Assignment Notes

1. **Generators for Space-Efficient Traversal**: In this project, you will employ Python `Generator` objects for tree traversal. This approach is notably space-efficient compared to returning a list of nodes (`List[Node]`), as it consumes _O(1)_ space instead of _O(n)_. Generators yield nodes sequentially and on-demand, providing a streamlined and memory-efficient solution. For a comprehensive introduction to Python generators, you can refer to [this article](https://realpython.com/introduction-to-python-generators/).

2. **Updating Heights and Balancing**: A common mistake in this project is the omission or incorrect update of node heights, as well as improper tree rebalancing within insert and remove functions. Be sure to meticulously read the notes provided under each function's description in the specifications. Consider how recursion and the call stack can be leveraged to rebalance the tree, especially in relation to the node you've just inserted or removed.

3. **Simplifying AVL Trees**: While AVL Trees are inherently complex, breaking down each function into specific cases or checks can significantly simplify the implementation. Consider all possible scenarios for each operation, such as checking if the node you're working on is the root or verifying the presence of a right node before proceeding with `node.right`. Ensure that you are updating the correct pointers throughout the process.

4. **Leveraging the Debugger**: Don’t hesitate to use the debugger; it is an invaluable tool, especially for deciphering the behavior of complex functions. Taking the time to familiarize yourself with its features will pay off, helping you verify whether your code is executing as expected and identifying any discrepancies in your logic.

5. **Avoiding Global Variables**: Utilizing global variables (with the `nonlocal` keyword) in your implementation will result in a deduction of 20 points.

6. **Maintaining Function Signatures**: Altering the signatures of provided functions will lead to a deduction of 2 points per instance, up to a maximum of 20 points.

## Assignment Specifications

#### class Node:

This class implements a tree node, utilized by the `BinarySearchTree` and `AVLTree` classes.

_DO NOT MODIFY the following attributes/functions._

- **Attributes**:

  - **`value: T`**: The value held by the `Node`. It can be of any type, such as `str`, `int`, `float`, `dict`, or even a more complex object.
  - **`parent: Node`**: A reference to this `Node`'s parent `Node`. It may be `None` if the node has no parent.
  - **`left: Node`**: A reference to this `Node`'s left child `Node`. It may be `None` if the node has no left child.
  - **`right: Node`**: A reference to this `Node`'s right child `Node`. It may be `None` if the node has no right child.
  - **`height: int`**: The number of levels of `Node`s below this one. The height of a leaf `Node` is considered to be 0.
  - **`data: Optional[str]`**: Value to be used as data for KNN Classifier.

- **Methods**:

  - **`__init__(self, value: T, parent: Node = None, left: Node = None, right: Node = None) -> None`**:

    - This constructor initializes an AVL Tree node with the provided values.
    - **Returns**: None.

  - **`__str__(self) -> str`** and **`__repr__(self) -> str`**:
    - These methods represent the `Node` as a string in the format `<value_held_by_node>`.
    - **Returns**: `str`.

#### class AVLTree

This class implements a self-balancing Binary Search Tree (BST) to ensure faster operation times.

##### Attributes (Do not modify)

- **origin (Node):** The root node of the AVLTree, which could potentially be `None`.
- **size (int):** The total number of nodes present in the AVLTree.

##### Methods (Do not modify)

- **`__init__(self) -> None`**: Creates an empty AVLTree.
- **`__str__(self) -> str`** and **`__repr__(self) -> str`**: Provides a string representation of the AVLTree.

##### Methods to Implement

- **height(self, root: Node) -> int:**

  - Calculates the height of a subtree in the AVL tree, handling cases where `root` might be `None`. The height of an empty subtree is defined as -1.
  - **Parameters:**
    - **root (Node):** The root node of the subtree whose height is being determined.
  - **Returns:** The height of the subtree rooted at `root`.
  - **Time / Auxiliary Space Complexity:** O(1) / O(1)

- **left_rotate(self, root: Node) -> Node**

  - Performs a left rotation on the subtree rooted at `root`, returning the new root after the rotation.
  - **Parameters:**
    - **root (Node):** The root node of the subtree to be rotated.
  - **Returns:** The new root of the rotated subtree.
  - **Time / Auxiliary Space Complexity:** O(1) / O(1)

- **right_rotate(self, root: Node) -> Node**

  - Performs a right rotation on the subtree rooted at `root`, returning the new root after the rotation.
  - Implementation is nearly identical to `left_rotate`, differing in a few lines of code.
  - **Parameters:**
    - **root (Node):** The root node of the subtree to be rotated.
  - **Returns:** The new root of the rotated subtree.
  - **Time / Auxiliary Space Complexity:** O(1) / O(1)

- **balance_factor(self, root: Node) -> int**

  - Computes the balance factor of the subtree rooted at `root`.
  - The balance factor is calculated as `h_L - h_R`, where `h_L` is the height of the left subtree, and `h_R` is the height of the right subtree.
  - In a properly balanced AVL tree, nodes should have a balance factor in {-1, 0, +1}. A balance factor of -2 or +2 requires rebalancing.
  - If `root` is `None`, the balance factor is 0.
  - To maintain efficiency, update the `height` attribute of each node during insertions, deletions, and rebalancing so that `h_L = left.height` and `h_R = right.height` can be used directly.
  - **Parameters:**
    - **root (Node):** The root node of the subtree for which the balance factor is computed.
  - **Returns:** The balance factor of `root`.
  - **Time / Auxiliary Space Complexity:** O(1) / O(1)

- **rebalance(self, root: Node) -> Node**

  - Rebalances the subtree rooted at `root` if it is unbalanced, returning the new root after rebalancing.
  - A subtree is considered unbalanced if `b >= 2 or b <= -2`, where `b` is the balance factor of `root`.
  - There are four possible imbalance cases, each requiring a specific sequence of rotations. More details can be found [here](https://en.wikipedia.org/wiki/AVL_tree#Rebalancing).
  - **Parameters:**
    - **root (Node):** The root of the subtree that may require rebalancing.
  - **Returns:** The new root of the rebalanced subtree.
  - **Time / Auxiliary Space Complexity:** O(1) / O(1)

- **insert(self, root: Node, val: T, data: string = None) -> Node**

  - Inserts a new node with value `val` into the subtree rooted at `root`, balancing the subtree as needed. Returns the root of the updated subtree.
  - If a node with value `val` already exists, the function does nothing.
  - Updates `size` and `origin` attributes of the `AVLTree`, sets correct parent/child pointers, updates node heights, and calls `rebalance` on affected ancestor nodes.
  - This method must be implemented recursively, otherwise you will lose all manual points on this one.
  - The recursive nature of this function contributes **O(log n) auxiliary space** due to the call stack. In addition to this, you are **not allowed** to allocate any additional space beyond what is necessary for standard function operations.
  - **Parameters:**
    - **root (Node):** The root of the subtree where `val` is inserted.
    - **val (T):** The value to be inserted.
    - **data (string):** Optional data value for use in KNN classification.
  - **Returns:** The root of the rebalanced subtree.
  - **Time / Auxiliary Space Complexity:** O(log n) / O(log n)

- **remove(self, root: Node, val: T) -> Node**

  - Removes the node with value `val` from the subtree rooted at `root`, balancing the subtree as needed. Returns the root of the updated subtree.
  - If `val` does not exist in the tree, the function does nothing.
  - Updates `size` and `origin` attributes, adjusts parent/child pointers, updates heights, and calls `rebalance` on affected ancestor nodes.
  - The removal process depends on whether the node has zero, one, or two children. For nodes with two children, swap with the predecessor (largest node in the left subtree), then recursively remove the predecessor.
  - This method must be implemented recursively, otherwise you will lose all manual points on this one.
  - Similar to `insert`, this function incurs **O(log n) auxiliary space** due to recursion, and you are **not allowed** to allocate additional space beyond what is necessary for function execution. This rule also applies to the `min`, `max`, and `search` functions below, as they all rely on recursion and their auxiliary space is determined by the call stack.
  - **Parameters:**
    - **root (Node):** The root of the subtree from which `val` is removed.
    - **val (T):** The value to be removed.
  - **Returns:** The root of the rebalanced subtree.
  - **Time / Auxiliary Space Complexity:** O(log n) / O(log n)

- **min(self, root: Node) -> Node**

  - Returns the `Node` containing the smallest value in the subtree rooted at `root`.
  - The implementation is straightforward when done recursively.
  - **Parameters:**
    - **root (Node):** The root of the subtree in which to search for the minimum value.
  - **Returns:** The `Node` holding the smallest value in the subtree.
  - **Time / Auxiliary Space Complexity:** O(log n) / O(log n)

- **max(self, root: Node) -> Node**

  - Returns the `Node` containing the largest value in the subtree rooted at `root`.
  - The implementation is similar to `min`, but searches the right subtree instead.
  - **Parameters:**
    - **root (Node):** The root of the subtree in which to search for the maximum value.
  - **Returns:** The `Node` holding the largest value in the subtree.
  - **Time / Auxiliary Space Complexity:** O(log n) / O(log n)

- **search(self, root: Node, val: T) -> Node**

  - Searches for a node with value `val` in the subtree rooted at `root`.
  - If `val` does not exist, returns the `Node` under which `val` would be inserted if added.
  - This method must be implemented recursively, otherwise you will lose all manual points on this one.
  - Example: In a tree with nodes `{1, 2, 3}` (2 as root), `search(node_2, 0)` returns `node_1`, as 0 would be inserted as `node_1`'s left child.
  - **Parameters:**
    - **root (Node):** The root of the subtree in which to search.
    - **val (T):** The value to search for.
  - **Returns:** The `Node` containing `val` if found, otherwise the potential parent node.
  - **Time / Auxiliary Space Complexity:** O(log n) / O(log n)

- **inorder(self, root: Node) -> Generator[Node, None, None]**

  - This function performs an inorder traversal (left, current, right) of the subtree rooted at `root`, generating the nodes one at a time using a [Python generator](https://realpython.com/introduction-to-python-generators/).
  - Use `yield` to produce individual nodes as they are encountered, and `yield from` for recursive calls to `inorder`.
  - Ensure that `None`-type nodes are not yielded.
  - **Important**: To pass the test case for this function, you must also make the AVLTree class iterable, enabling the usage of `for node in avltree` to iterate over the tree in an inorder manner.
  - **Time Complexity:** O(n), as the entire tree is traversed.
  - **Auxiliary Space Complexity:** O(log n). The recursive nature of this function contributes **O(log n) auxiliary space** due to the call stack. In addition to this, you are **not allowed** to allocate any additional space beyond what is necessary for standard function operations. This applies similarly to `preorder` and `postorder` traversals.
  - **Parameters:**
    - **root (Node):** The root node of the current subtree being traversed.
  - **Returns:** A generator yielding the nodes of the subtree in inorder.

- \***\*iter**(self) -> Generator[Node, None, None]\*\*

  - This method makes the AVL tree class iterable, allowing you to use it in loops like `for node in tree`.
  - For the iteration to work, this function should be implemented such that it returns the generator from the inorder traversal of the tree.
  - **Returns:** A generator yielding the nodes of the tree in inorder.
  - **Implementation Note:** This function should be one line, calling the `inorder` function.

- **preorder(self, root: Node) -> Generator[Node, None, None]**

  - This function performs a preorder traversal (current, left, right) of the subtree rooted at `root`, generating the nodes one at a time using a [Python generator](https://realpython.com/introduction-to-python-generators/).
  - Use `yield` to produce individual nodes as they are encountered, and `yield from` for recursive calls to `preorder`.
  - Ensure that `None`-type nodes are not yielded.
  - **Time Complexity:** O(n), as the entire tree is traversed.
  - **Auxiliary Space Complexity:** O(log n). The recursive nature of this function contributes **O(log n) auxiliary space** due to the call stack. In addition to this, you are **not allowed** to allocate any additional space beyond what is necessary for function execution.
  - **Parameters:**
    - **root (Node):** The root node of the current subtree being traversed.
  - **Returns:** A generator yielding the nodes of the subtree in preorder.

- **postorder(self, root: Node) -> Generator[Node, None, None]**

  - This function performs a postorder traversal (left, right, current) of the subtree rooted at `root`, generating the nodes one at a time using a [Python generator](https://realpython.com/introduction-to-python-generators/).
  - Utilize `yield` to produce individual nodes as they are encountered, and `yield from` for recursive calls to `postorder`.
  - Ensure that `None`-type nodes are not yielded.
  - **Time Complexity:** O(n), as the entire tree is traversed.
  - **Auxiliary Space Complexity:** O(log n). The recursive nature of this function contributes **O(log n) auxiliary space** due to the call stack. As with `inorder` and `preorder`, you are **not allowed** to allocate any additional space beyond what is necessary for function execution.
  - **Parameters:**
    - **root (Node):** The root node of the current subtree being traversed.
  - **Returns:** A generator yielding the nodes of the subtree in postorder. A `StopIteration` exception is raised once all nodes have been yielded.

- **levelorder(self, root: Node) -> Generator[Node, None, None]**
  - This function performs a level-order (breadth-first) traversal of the subtree rooted at `root`, generating the nodes one at a time using a [Python generator](https://realpython.com/introduction-to-python-generators/).
  - Use the `queue.SimpleQueue` class for maintaining the queue of nodes during the traversal. [Refer to the official documentation for more information.](https://docs.python.org/3/library/queue.html#queue.SimpleQueue)
  - Utilize `yield` to produce individual nodes as they are encountered.
  - Ensure that `None`-type nodes are not yielded.
  - **Time / Space Complexity:** O(n) / O(n). The entire tree is traversed, and due to the nature of level-order traversal, the queue can grow to O(n), particularly in a [perfect binary tree](https://www.programiz.com/dsa/perfect-binary-tree) scenario.
  - **Parameters:**
    - **root (Node):** The root node of the current subtree being traversed.
  - **Returns:** A generator yielding the nodes of the subtree in level-order. A `StopIteration` exception is raised once all nodes have been yielded.

## Application: K-th Nearest Neighbor Classifier

Congratulations! You’ve just won a prestigious hackathon at Silicon Valley's top tech event. As a prize, a high-tech startup has offered you an internship with their Data Intelligence team. Your first challenge? Build a tool that predicts the success of marketing campaigns. Your tool will be a game-changer for the company’s growth strategy!

To accomplish this, you decided to use an **AVL Tree** to implement a **classifier**, a data structure-based approach to predicting outcomes.

### What is a Classifier?

A classifier processes **training data**, where each data point consists of a numerical parameter and a corresponding classification label. Essentially, it learns from past data to classify new, unseen data points. For example:

> "In the past, when my parameter `x` was `0.4`, the outcome was `y`."

Using this knowledge, a classifier can predict classifications for new values based on patterns in the training data. This is one of the fundamental concepts in machine learning, allowing predictions to be made based on historical patterns.

### K-Nearest Neighbor (KNN) Classifier

Your classifier will use the **K-Nearest Neighbor (KNN) algorithm**, which is simpler than it sounds. Here’s how it works:

1. Given a set of training data points, when a new data point needs classification, the algorithm identifies the **k** closest data points (neighbors) to the new value.
2. The classification of the new point is determined based on the most common classification among these **k** neighbors, weighted by proximity.

In simpler terms, the algorithm assumes that **similar points will likely have similar classifications**. If a new data point is close to data labeled `A`, it will likely also be classified as `A`.

### Example Application

Your boss wants you to use the classifier to predict whether the **next marketing campaign will be successful** based on past data about a designer’s mood and previous campaign outcomes.

You are required to implement the **KNNClassifier** class with the following specifications:

---

#### `class KNNClassifier:`

A classifier that uses the K-Nearest Neighbors (KNN) algorithm to classify new data points.

### **DO NOT MODIFY THE FOLLOWING:**

- **Attributes:**

  - `k: int` — The number of neighbors to consider for classification.
  - `tree: AVLTree` — An empty AVL Tree that will store the training data.

- **Methods:**

  - `__init__(self, k: int) -> None`

    - Initializes `k` and an empty AVL Tree.

  - `floats_equal(self, f1: float, f2: float) -> bool`
    - Compares two floats, accounting for floating-point precision errors.
    - **Parameters:**
      - `f1`: First float to compare.
      - `f2`: Second float to compare.
    - **Returns:** `True` if they are approximately equal, `False` otherwise.

---

### **Functions to Implement:**

- **`train(self, data: List[Tuple[float, str]]) -> None`**
  - Trains the classifier by inserting each data point into the AVL tree.
  - The first element of each tuple is the **node value**, and the second element is stored as the **data attribute** of the node.
  - **Important:** Do **NOT** manually create a `Node` object—use the AVL Tree’s `insert` method.
  - **Performance:**
    - **Time Complexity:** O(n log n) — Each insertion into the AVL tree takes O(log n), repeated for `n` elements.
    - **Auxiliary Space Complexity:** O(1)
  - **Parameters:**
    - `data`: List of tuples (`value`, `classification`).
  - **Returns:** `None`.
  - **Tip:** This function should be short—only **two lines of code** are needed.
  - **Guarantee:** No two data points will have the same float value.

---

- **`get_k_neighbors(self, value: float) -> List[Tuple[float, str]]`**
  - Finds the **k** closest neighbors to the given value using absolute differences.
  - Neighbors with the same absolute difference to the value should **not** be included as ties are ignored.
  - **Important:** Use `self.floats_equal` when comparing floats to handle precision issues.
  - **Performance:**
    - **Time Complexity:** O(n) — Requires scanning the tree.
    - **Auxiliary Space Complexity:** O(n) — Stores up to `n` elements.
  - **Parameters:**
    - `value`: The value for which to find the closest neighbors.
  - **Returns:** A list containing the **k** closest neighbors in the form (`node_value`, `node_classification`).
  - **Tip:** Consider breaking this function into helper methods for clarity.

---

- **`calculate_best_fit(self, neighbors: List[Tuple[float, str]], value: float) -> str`**
  - Determines the most likely classification for a given value based on **neighbor weighting**.
  - Each neighbor’s influence is weighted as **1 / abs(value - node_value)**.
  - The classification with the **highest cumulative weight** is chosen as the final classification.
  - **Performance:**
    - **Time Complexity:** O(n) — Iterates through `n` neighbors.
    - **Auxiliary Space Complexity:** O(n) — Stores classification counts.
  - **Parameters:**
    - `neighbors`: A list of (`node_value`, `node_classification`) tuples.
    - `value`: The value to classify.
  - **Returns:** The **most likely classification** as a string.

---

- **`classify(self, value: float) -> str`**
  - Classifies a given value using the **k-nearest neighbors** method.
  - This function should call:
    1. `get_k_neighbors(value)` to find the closest neighbors.
    2. `calculate_best_fit(neighbors, value)` to determine the classification.
  - **Performance:**
    - **Time Complexity:** O(n) — Dependent on `get_k_neighbors` and `calculate_best_fit`.
    - **Auxiliary Space Complexity:** O(n) — Stores neighbors and weights.
  - **Parameters:**
    - `value`: The value to classify.
  - **Returns:** The **predicted classification** as a string.
  - **Tip:** Keep this function concise; it mainly orchestrates the previous functions.

---

### **Final Notes:**

- Make sure your implementation efficiently retrieves the closest neighbors and accurately calculates weighted classifications.
- Avoid unnecessary complexity—each function should have a **clear** and **direct** purpose.
- **Use helper functions** where necessary to improve readability and maintainability.

### Examples:

#### Example 1:

In all examples, **"L"** represents a loss in the marketing campaign, while **"W"** represents a win.

```python
data = [(0.1, "L"), (0.2, "L"), (0.6, "W"), (0.7, "W"), (0.5, "W")]
classifier = KNNClassifier(k=2)
classifier.train(data)
self.assertEqual("W", classifier.classify(0.55))
```

Here, after training, the classifier searches for the **two closest neighbors** to `0.55`. The closest neighbors are:

```
[(0.2, "L"), (0.7, "W")]
```

The classification is determined using the weighting formula **1/d**, where `d` is the absolute difference between the value to classify and each neighbor. The neighbor `(0.7, "W")` has a **larger weight**, leading the classifier to predict a **Win** (`"W"`).

**Important:** The values `0.6` and `0.5` are ignored because they are equidistant (tied in distance). As per the specification, **ties are ignored** and not included in the neighbor selection.

---

#### Example 2:

```python
data = [(0.1, "L"), (0.2, "L"), (0.6, "W"), (0.7, "W")]
classifier = KNNClassifier()
classifier.train(data)
self.assertIsNone(classifier.classify(0.4))
```

In this case, all the **closest neighbors have the same distance** to `0.4`. Since **ties must be ignored**, no neighbors can be used for classification. As a result, the classifier **returns `None`**, indicating that a prediction is not possible.

---

#### Example 3:

```python
data = [(0.1, "L"), (0.2, "L"), (0.6, "W"), (0.7, "W"), (0.5, "L")]
classifier = KNNClassifier()
classifier.train(data)
self.assertEqual("L", classifier.classify(0.4))
```

Here, an **additional data point (`0.5, "L"`)** is included in the training set. Because `0.5` is **closer** to `0.4` than the previous data points, it **breaks the tie** and becomes a significant neighbor. The classifier now has a stronger influence from `"L"` values, leading to a predicted classification of **Loss (`"L"`)**.

## The end!

![joke](img/tree.jpg)

# **Submission Guidelines**

### **Deliverables:**

For each project, a `solution.py` file will be provided. Ensure to write your Python code within this file. For best results:

- 📥 **Download** both `solution.py` and `tests.py` to your local machine.
- 🛠️ Use **PyCharm** for a smoother coding and debugging experience.

### **How to Work on a Project Locally:**

Choose one of the two methods below:

---

#### **APPROACH 1: Using D2L for Starter Package**

1. 🖥️ Ensure PyCharm is installed.
2. 📦 **Download** the starter package from the _Projects_ tab on D2L. _(See the tutorial video on D2L if needed)_.
3. 📝 Write your code and, once ready, 📤 **upload** your `solution.py` to Codio. _(Refer to the D2L tutorial video for help)_.

---

#### **APPROACH 2: Directly from Codio**

1. 📁 On your PC, create a local folder like `Project01`.
2. 📥 **Download** `solution.py` from Codio.
3. 📥 **Download** `tests.py` from Codio for testing purposes.
4. 🛠️ Use PyCharm for coding.
5. 📤 **Upload** the `solution.py` back to Codio after ensuring the existing file is renamed or deleted.
6. 🔚 Scroll to the end in Codio's Guide editor and click the **Submit** button.

---

**Tip:** While Codio can be used, we recommend working locally for a superior debugging experience in PyCharm. Aim to finalize your project locally before submitting on Codio.

---

### **Important:**

- Always **upload** your solution and **click** the 'Submit' button as directed.
- All project submissions are due on Codio. **Any submission after its deadline is subject to late penalties** .

### **Grading:**

**Note on Comprehensive Testing:**

If your solution fails to pass a comprehensive test for a specific function during our assessment, **half of the manual
points allocated for that function will be deducted**. This is to emphasize the importance of not only meeting basic
requirements but also ensuring robustness and correctness in your code. Consider these comprehensive tests as tools for
ensuring quality and resilience in your solutions.

**Additional Note on Scenario Generation:**

While we make every effort to generate test cases that encompass every possible scenario, there might be times when some edge cases are inadvertently overlooked. Nevertheless, should we identify any scenario where your submitted logic doesn't hold, even if it's not part of our provided test cases, we reserve the right to deduct from the manual points. This highlights the significance of crafting logic that doesn't merely pass the given tests, but is genuinely resilient and correctly addresses the problem's entirety. Always strive to think beyond the provided cases, ensuring that your solutions are comprehensive and robust.

**Docstrings:**

Docstrings are not provided for this project. Please use Project 1 as a template for your docstrings.
To learn more on what docstrings are, visit the following
website: [What are Docstrings?](https://peps.python.org/pep-0257/)
Each missing docstring is a 1 point deduction, up to 5 points of deductions

- Tests (70)

  - `AVLTree`: \_\_/44
    - `rotate`: \_\_/5
    - `balance_factor`: \_\_/1
    - `rebalance`: \_\_/7
    - `insert`: \_\_/7
    - `remove`: \_\_/7
    - `min`: \_\_/1
    - `max`: \_\_/1
    - `search`: \_\_/5
    - `inorder`/`__iter__`: \_\_/1
    - `preorder`: \_\_/1
    - `postorder`: \_\_/1
    - `levelorder`: \_\_/1
    - `avl_comprehensive`: \_\_/6
  - `KNNClassifier`: \_\_/26
    - `test_train`: \_\_/5
    - `test_get_k_neighbors`: \_\_/5
    - `test_calculate_best_fit`: \_\_/5
    - `test_knn`: \_\_/11

- Manual (32)

  - Time and space complexity points are **all-or-nothing** for each function. If you fail to meet time **or** space complexity in a given function, you do not receive manual points for that function.
  - For AVL tree, the **insert**, **remove**, **search** methods must be implemented recursively, otherwise no manual points will be awarded to the corresponding method.
  - Loss of 2 points per changed function signature (max 20 point loss).
  - Loss of 20 points (flat-rate) for use of global variables (with the nonlocal keyword).
  - Each missing docstring is a 1 point deduction, up to 5 points of deductions.
  - Loss of half manual points all functions if large comprehensive test where the data structure's primary methods are tested fails.
  - Loss of all manual points for not using the data structure built for the application problem.

    - `AVLTree` time & space: \_\_/20
      - `left_rotate`: \_\_/2
      - `right_rotate`: \_\_/2
      - `balance_factor`: \_\_/1
      - `rebalance`: \_\_/2
      - `insert`: \_\_/3
      - `remove`: \_\_/3
      - `min`: \_\_/1
      - `max`: \_\_/1
      - `search`: \_\_/1
      - `inorder`/`__iter__`: \_\_/1
      - `preorder`: \_\_/1
      - `postorder`: \_\_/1
      - `levelorder`: \_\_/1
    - `KNNClassifier`: time & space: \_\_/12
      - `train`: \_\_/3
      - `get_k_neighbors`: \_\_/3
      - `calculate_best_fit`: \_\_/3
      - `classify`: \_\_/3
