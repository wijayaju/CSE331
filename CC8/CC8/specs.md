

## Retrieve  Kth Largest Node in a BST


Create a function that takes in a Binary Search Tree (BST) and a positive integer `k`, returning the kth largest integer value within the BST.

Assume that the BST only contains integer values and that `k` will always be less than or equal to the total number of nodes in the tree.

For this question, duplicate integers are treated as distinct entries. For instance, in a BST with values `{5, 7, 7}`, the second largest value would be `7`—not `5`.

Each **BST** node has an integer `value`, a `left` child node, and a `right` child node. A node is a valid **BST** node only if it adheres to the BST properties: its `value` is strictly greater than all values of nodes in its left subtree, and less than or equal to all values of nodes in its right subtree. The children nodes are either valid **BST** nodes themselves or `None` / `null`.

### Sample Input

```plaintext
tree =   15
        /    \
       5      20
      / \    /  \
     2   5  17   22
    / \
   1   3
k = 3
```

### Sample Output

```plaintext
17
```

Few more additional examples:

---

### Example 1
#### Sample Input
```plaintext
tree =   10
        /    \
       5      15
      / \    /  \
     2   7  13   20
    /       \
   1         14
k = 2
```

#### Sample Output
```plaintext
15
```

---

### Example 2
#### Sample Input
```plaintext
tree =   25
        /    \
       10     30
      /  \    /  \
     5   15  28   35
        /  \
       12   20
k = 4
```

#### Sample Output
```plaintext
20
```

---

### Example 3
#### Sample Input
```plaintext
tree =   8
        /   \
       3     10
      / \      \
     1   6      14
        /  \    /
       4    7  13
k = 5
```

#### Sample Output
```plaintext
6
```










---

### Tip 1
Remember, the tree provided is a Binary Search Tree (BST), not just any Binary Tree. How might this property help you design a solution that improves time efficiency?

### Tip 2
One straightforward solution is to perform an in-order traversal of the BST and gather all node values in the order they are visited. Since in-order traversal retrieves BST values in ascending order, you could then take the `k`th value from the end to get the `k`th largest value.

### Tip 3
There’s a way to solve this problem more efficiently in (O(h + k)) time, where (h) is the height of the tree. Instead of traversing nodes in ascending order, consider examining them in descending order.

### Tip 4
To implement the (O(h + k)) solution from the previous strategy, perform a reverse in-order traversal of the tree. By visiting nodes in descending order, you can simply return the `k`th node you encounter.

### Space & Time Complexity
**Time Complexity:** (O(h + k))  
**Space Complexity:** (O(h)), where (h) is the tree's height and (k) is the given input.







