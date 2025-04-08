

## 🔍 Multi String Search

<img src="img/data1.png" alt="Trie Search Diagram" width="400"/>




### 🧾 Problem Statement

Implement a function that accepts a large string and a list of smaller strings, each shorter than the large string. The function should return a list of boolean values. Each boolean should indicate whether the respective smaller string appears anywhere in the large string.

**Restrictions:**  
You are **not allowed** to use any built-in string search or matching functions provided by your programming language.

---

### 💡 Suggested Approaches

- A straightforward method is to loop over each small string and, for each one, iterate through the characters of the large string to check for a match using nested loops. Consider whether this method is efficient from a time complexity standpoint.

- Another approach is to create a data structure similar to a suffix trie that stores all possible suffixes of the large string. You can then check each small string against this structure. Think about how this impacts both time and memory usage.

- Alternatively, you can construct a trie using all the small strings. Then, traverse the large string character by character, checking whether any substring matches one of the small strings by searching through the trie. Compare the efficiency of this method to the one above.




✅ **Example 1: Basic Matches**  
```python
big_string = "abcde"
small_strings = ["a", "ab", "e", "de", "xyz"]
```
**Output:**  
```python
[True, True, True, True, False]
```

---

✅ **Example 2: Overlapping Substrings**  
```python
big_string = "abababa"
small_strings = ["aba", "bab", "ab", "ba"]
```
**Output:**  
```python
[True, True, True, True]
```

---

✅ **Example 3: Repeated Queries**  
```python
big_string = "repeatrepeat"
small_strings = ["repeat", "repeat", "eat", "rep"]
```
**Output:**  
```python
[True, True, True, True]
```

## 🧠 Optimal Time & Space Complexity

- **Time Complexity:** O(ns + bs)  
- **Space Complexity:** O(ns)

Where:  
- `n` = total number of small strings  
- `s` = length of the longest small string  
- `b` = length of the large string






<img src="img/API.png" alt="API" width="400"/>


























