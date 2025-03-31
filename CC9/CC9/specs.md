

## Disjoint Set Manager

The **disjoint-set manager** (also called **union-find** structure) is similar to a traditional set structure. It manages a collection of unique values, but these values are distributed across different sets, ensuring that no value belongs to more than one set at the same time.

Your task is to implement a `DisjointSet` class that handles the following operations:

- **add_set(value)**: Creates a new set containing the given `value`.  
- **merge_sets(value_one, value_two)**: Takes two values and merges their sets if they belong to different sets. If either of the values does not exist in any set or they are already in the same set, this operation does nothing.
- **find_representative(value)**: Returns the representative of the set containing the `value`. This should always be the same representative for every member of a set. If the `value` does not exist in any set, return `None`. Note that when sets merge, the representative might change.

You can assume that **add_set** will never be called with the same value twice.

### Example Usage

```python
dsm = DisjointSet()
dsm.add_set(5)  # null
dsm.add_set(10)  # null
dsm.find_representative(5)  # 5
dsm.find_representative(10)  # 10
dsm.merge_sets(5, 10)  # null
dsm.find_representative(5)  # 5
dsm.find_representative(10)  # 5
dsm.add_set(20)  # null
dsm.find_representative(20)  # 20
dsm.merge_sets(20, 10)  # null
dsm.find_representative(5)  # 5
dsm.find_representative(10)  # 5
dsm.find_representative(20)  # 5
```

---

### Hints for Disjoint Set Manager

#### Hint 1
Disjoint sets traditionally use a tree-like structure for each set, with the root node being the **representative** node returned by `find_representative`.

#### Hint 2
When combining two trees with `merge_sets`, ensure that the height of the resulting tree is minimized. This will help maintain a logarithmic time complexity for operations.

#### Hint 3
As the height of the tree increases, time complexity worsens. You can reduce tree height by making all nodes point directly to the root during the `find_representative` operation. This technique is known as **path compression**.

#### Optimal Space & Time Complexity
- **add_set** method: O(1) time | O(1) space
- **merge_sets** and **find_representative** methods: O(α(n)), approximately O(1) time | O(α(n)), approximately O(1) space, where **n** is the total number of values.






### Explanation of Time and Space Complexity for `merge_sets` and `find_representative`

When we say the **time complexity** of `merge_sets` and `find_representative` methods is **O(α(n))**, approximately **O(1)**, it means that these operations are very efficient, almost constant time for all practical purposes. 



#### 1. What is O(α(n))?
- The **α(n)** (pronounced "inverse Ackermann function") is a function that grows *extremely* slowly. In fact, for all inputs you’ll likely deal with (even if `n` is in the millions or billions), **α(n)** is less than or equal to 5. This makes **α(n)** very close to a constant, which is why we say the operation is "approximately O(1)".
- Even though the formal complexity is **O(α(n))**, in practice, you can think of it as **constant time**, because the Ackermann function grows so slowly that the difference is negligible.

#### 2. Approximately O(1) Time
- **O(1)** means constant time, which means the operation takes the same amount of time no matter how many elements (`n`) are in the set.
- So, when we say **O(α(n)), approximately O(1)**, we are basically saying that even though there's a formal mathematical upper bound of **α(n)**, it behaves like a constant time operation in practice.

#### 3. Approximately O(1) Space
- The space complexity is also **approximately O(1)**, which means that `merge_sets` and `find_representative` do not require extra space that depends on the number of values `n`. The amount of memory used by these operations remains almost constant regardless of the input size.

#### Putting it together:
For all practical purposes, **`merge_sets`** and **`find_representative`** are extremely fast operations, almost as fast as **constant time** (O(1)), and they don’t take up much additional memory when performing their tasks.

