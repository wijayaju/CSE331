## Balanced Brackets Challenge

### Problem Statement
You are given a string containing different types of brackets: `()`, `{}`, and `[]`. Your task is to implement a function that determines whether the given string contains a properly balanced sequence of brackets. 

A sequence is considered balanced if:
- Each opening bracket has a corresponding and correctly ordered closing bracket.
- Brackets are properly nested, meaning no closing bracket appears before its matching opening bracket.
- The sequence does not contain unmatched brackets.

Write a function that takes a string as input and returns `True` if the brackets are balanced, otherwise `False`.

### Function Signature
```python
 def balanced_brackets(string: str) -> bool:
```

### Input
- `string` (str): A sequence that may contain any of the characters `()[]{}` along with other characters.

### Output
- Returns a boolean (`True` or `False`) indicating whether the brackets in the string are balanced.

### Constraints
- The input string length will be between `0` and `10^5`.

### Example Test Cases
#### Test Case 1
**Input:**
```python
balanced_brackets("([])(){}(())()()")
```
**Output:**
```python
True
```

#### Test Case 2
**Input:**
```python
balanced_brackets("([)]")
```
**Output:**
```python
False
```

#### Test Case 3
**Input:**
```python
balanced_brackets("(({{[[[]]]}}))")
```
**Output:**
```python
True
```

#### Test Case 4
**Input:**
```python
balanced_brackets("({[})")
```
**Output:**
```python
False
```


