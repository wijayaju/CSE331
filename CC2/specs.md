

## Smallest Subarray to Sort the Entire Array

### Problem Statement

Write a function that takes an array of at least two integers and returns an array containing the starting and ending indices of the smallest subarray that needs to be sorted in place for the entire input array to be sorted in ascending order. 

If the input array is already sorted, the function should return `[-1, -1]`.

### Example

**Input:**

```python
array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
```

**Output:**

```python
[3, 9]
```

### Requirements

- The function should handle arrays of varying lengths but must contain at least two integers.
- Ensure the function can determine if the array is already sorted and handle this case appropriately by returning `[-1, -1]`.

### 
- **Expected Runtime Complexity:** \( O(n) \)
- **Expected Space Complexity:** \( O(1) \)
- Please note that CCs are not manually graded, check the released solution after the CC is closed to compare your work. 

### Constraints

- The array will contain at least two integers.
- The elements of the array are not guaranteed to be unique.
- The function should aim for optimal time complexity.

### Additional Information

- Assume that the input array will contain only integers.
- Focus on writing clean, efficient, and well-documented code.