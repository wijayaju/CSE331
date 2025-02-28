# Assignment: Recursive Techniques in Singly Linked List

Recursion is a cornerstone of computer science, offering a way to solve intricate problems by breaking them down into simpler tasks. This project concentrates on the application of recursion to implement and manipulate a Singly Linked List (SLL).

![Recursion Image](img/rec.jpeg)

### Introduction:

The project employs **two primary recursive approaches**:
1. Functions that incorporate an inner function responsible for recursion.
2. Functions that are intrinsically recursive themselves.

**Remember**: Every function you design must employ recursion.

For a deeper understanding of inner functions, check out this [article](https://realpython.com/inner-functions-what-are-they-good-for/).

For comprehensive knowledge on Singly Linked Lists, review [Zybooks Chapter 20](https://learn.zybooks.com/zybook/MSUCSE331OnsayFall2022/chapter/20/section/2).

### Singly Linked Lists:

A Singly Linked List (SLL) is a collection of nodes where each node contains a data element and a reference to the next node in the sequence.

**Head Reference of a Singly Linked List:**
![SLL with Head](img/SLL_H.png)

The SLL in this project holds references to both the **Head** and **Tail**.
![SLL with Head and Tail](img/SLL_H_T.png)

While SLLs offer benefits like rapid insertion and deletion, they lack direct indexing capabilities, necessitating traversal for element access.



### **`class Node:`**

**Do not modify this class.**

- **Attributes:**
    - `value`: Contains the value stored in a Node.
    - `next`: Points to the subsequent Node (Defaults to None).

- **Methods:**
    - `__init__(self, value: T, next: Node = None) -> None`: Initializes a node with the specified `value` and `next` reference.
    - `__repr__(self) -> str`: Represents a node as a string in the format 'value'.
    - `__str__(self) -> str`: Returns the string representation of the node. Use `str(node)` for conversion.
    - `__eq__(self, other: Node) -> bool`: Compares two Nodes, returning True or False based on equality.

---

### **`class RecursiveSinglyLinkedList:`**

**Preserve the attributes and methods below without modification.**

- **Attributes:**
    - `head`: Points to the initial Node in the list (Defaults to None).
    - `tail`: Points to the final Node in the list (Defaults to None).

- **Methods:**
    - `__init__(self) -> None`: Initializes an instance of the RecursiveSinglyLinkedList.
    - `__repr__(self) -> str`: Returns a string representation of the list. Implementation depends on the `to_string` method.
    - `__eq__(self, other: SLL) -> bool`: Compares two RecursiveSinglyLinkedLists, returning True or False based on equality.

---

**Required Implementations in `solution.py`:**

1. **`add(self, value: T, back: bool = True) -> None`**:
   - Inserts `value` into the list.
   - If `back` is true, insert at the list's end; otherwise, at the front.
   - Time complexity: O(1).

2. **`remove(self, value: T) -> bool`**:
   - Removes the first occurrence of `value` in the list.
   - Returns True if removal is successful, otherwise False.
   - Must invoke the helper function `remove_inner`.
   - Time complexity: O(n).

3. **`remove_inner(curr: Node) -> Tuple[Node, bool]`**:
   - Initiating at head `curr`, removes the first occurrence of `value` from the `remove` function.
   - Returns a tuple: list's head and a boolean indicating removal success.
   - Refer to [this article](https://realpython.com/inner-functions-what-are-they-good-for/) for more on inner functions.
   - Time complexity: O(n).

4. **`search(self, value: T) -> bool`**:
   - Searches for `value` in the list.
   - Returns True if found, otherwise False.
   - Must invoke the helper function `search_inner`.
   - Time complexity: O(n).

5. **`search_inner(curr: Node) -> bool`**:
   - Starting at head `curr`, searches for `value` from the `search` function.
   - Returns True if found, otherwise False.
   - Time complexity: O(n).

6. **`to_string(self, curr: Node) -> str`**:
   - Generates a string representation of the list starting from head `curr`.
   - Values are separated by " -->", with no trailing separator.
   - Returns "None" if the list is empty.
   - Time complexity: O(n) (assuming string concatenation is O(1)).

---

### **SLL Recursion Problem**:

- **`remove_duplicates(self, curr: Node) -> None`**:
   - Eliminates duplicates from a sorted singly linked list.
   - Time complexity: O(n).

---

### **Additional Challenge**:

- **`fibonacci(n: int, cache: dict) -> int`**:
   - Calculates the nth Fibonacci number using the provided dictionary as a cache.
   - For example:
     - fibonacci(0)=0
     - fibonacci(1)=1
     - fibonacci(2)=1
     - fibonacci(3)=2
     - fibonacci(4)=3
     - fibonacci(5)=5
   - Time complexity: O(n).



{SUBMIT!|assessment}(test-3379255259)















