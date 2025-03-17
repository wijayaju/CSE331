
# **Tree Branch Summation**


### **Objective**
Write a function that takes in a **Binary Tree** and returns a **list of its branch sums** in order from the leftmost branch to the rightmost branch.

![alt text](onezero.jpeg)

### **Definitions**
- A **branch sum** is the sum of all node values in a branch of the Binary Tree.
- A **branch** is a path starting from the **root node** and ending at any **leaf node**.
- Each node in the Binary Tree has:
  - An **integer value**.
  - A **left child node** (which could be another BinaryTree node or `None`).
  - A **right child node** (which could be another BinaryTree node or `None`).

---

### **Example 1**

#### **Input:**
```plaintext
tree = 
       1
     /   \
    2     3
   / \   / \
  4   5 6   7
 / \  /
8   9 10
```

#### **Output:**
```plaintext
[15, 16, 18, 10, 11]
```

#### **Explanation:**
1. **Branch:** `1 → 2 → 4 → 8` → Sum = `1 + 2 + 4 + 8 = 15`
2. **Branch:** `1 → 2 → 4 → 9` → Sum = `1 + 2 + 4 + 9 = 16`
3. **Branch:** `1 → 2 → 5 → 10` → Sum = `1 + 2 + 5 + 10 = 18`
4. **Branch:** `1 → 3 → 6` → Sum = `1 + 3 + 6 = 10`
5. **Branch:** `1 → 3 → 7` → Sum = `1 + 3 + 7 = 11`

---

### **Example 2**

#### **Input:**
```plaintext
tree =
       10
      /  \
     5    20
    / \     \
   3   8     25
```

#### **Output:**
```plaintext
[18, 23, 55]
```

#### **Explanation:**
1. **Branch:** `10 → 5 → 3` → Sum = `10 + 5 + 3 = 18`
2. **Branch:** `10 → 5 → 8` → Sum = `10 + 5 + 8 = 23`
3. **Branch:** `10 → 20 → 25` → Sum = `10 + 20 + 25 = 55`

---

### **Example 3**

#### **Input:**
```plaintext
tree =
      7
       \
        12
       /  \
      5    15
```

#### **Output:**
```plaintext
[24, 34]
```

#### **Explanation:**
1. **Branch:** `7 → 12 → 5` → Sum = `7 + 12 + 5 = 24`
2. **Branch:** `7 → 12 → 15` → Sum = `7 + 12 + 15 = 34`

---

### **Hints:**
1. Traverse the Binary Tree in a **depth-first search (DFS) manner**.
2. Maintain a **running sum** as you traverse the tree.
3. When you reach a **leaf node** (a node with no children), **store the computed sum** in a list.
4. Use **recursion** to pass the updated sum to child nodes.

---

### **Expected Complexity**
- **Time Complexity:**  O(n) \, where  n  is the number of nodes.
- **Space Complexity:**  O(n) , considering recursion depth and the storage of sums.

---