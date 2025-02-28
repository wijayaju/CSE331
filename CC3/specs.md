## LRU Cache

### Problem Statement

Implement a class `LRUCache` for a Least Recently Used (LRU) cache. The class should support the following methods:

- `insert_key_value_pair(key, value)`: Inserts a key-value pair into the cache.
- `get_value_from_key(key)`: Retrieves the value associated with the provided key.
- `get_most_recent_key()`: Retrieves the most recently used key (either recently inserted or retrieved).

All these methods should run in **O(1)** time complexity.

Additionally, the `LRUCache` class should have a `max_size` attribute, which represents the maximum number of key-value pairs the cache can hold. This value should be passed as an argument when creating an instance of the cache.

When inserting a new key-value pair and the cache has reached its capacity, the least recently used key-value pair should be evicted. Note that if the key already exists, its value should be updated, and this should not trigger an eviction.

If a key that does not exist is queried using `get_value_from_key`, the method should return `None`.

### Method Details

1. **`insert_key_value_pair(key, value)`**:
   - Inserts or updates the given key-value pair in the cache.
   - If the cache is at maximum capacity, it evicts the least recently used key-value pair.

2. **`get_value_from_key(key)`**:
   - Returns the value associated with the given key, or `None` if the key does not exist.

3. **`get_most_recent_key()`**:
   - Returns the most recently used key in the cache.

### Constraints

- The cache should handle keys and values of any data type.
- All operations should have a **O(1)** time complexity.


## LRU Cache

### Problem Statement

Implement a class `LRUCache` for a Least Recently Used (LRU) cache. The class should support the following methods:
![alt text](.guides/img/LRUCache.png)

- `insert_key_value_pair(key, value)`: Inserts a key-value pair into the cache.
- `get_value_from_key(key)`: Retrieves the value associated with the provided key.
- `get_most_recent_key()`: Retrieves the most recently used key (either recently inserted or retrieved).

All these methods should run in **O(1)** time complexity.

Additionally, the `LRUCache` class should have a `max_size` attribute, which represents the maximum number of key-value pairs the cache can hold. This value should be passed as an argument when creating an instance of the cache.

When inserting a new key-value pair and the cache has reached its capacity, the least recently used key-value pair should be evicted. Note that if the key already exists, its value should be updated, and this should not trigger an eviction.

If a key that does not exist is queried using `get_value_from_key`, the method should return `None`.

### Method Details

1. **`insert_key_value_pair(key, value)`**:
   - Inserts or updates the given key-value pair in the cache.
   - If the cache is at maximum capacity, it evicts the least recently used key-value pair.

2. **`get_value_from_key(key)`**:
   - Returns the value associated with the given key, or `None` if the key does not exist.

3. **`get_most_recent_key()`**:
   - Returns the most recently used key in the cache.

### Constraints

- The cache should handle keys and values of any data type.
- All operations should have a **O(1)** time complexity.

### Examples

#### Example 1
```python
cache = LRUCache(2)
cache.insert_key_value_pair(1, 'A')
cache.insert_key_value_pair(2, 'B')
print(cache.get_value_from_key(1))  # Output: 'A'
cache.insert_key_value_pair(3, 'C')
print(cache.get_value_from_key(2))  # Output: None (2 was evicted)
print(cache.get_value_from_key(3))  # Output: 'C'
```

#### Example 2
```python
cache = LRUCache(3)
cache.insert_key_value_pair("apple", 10)
cache.insert_key_value_pair("banana", 20)
cache.insert_key_value_pair("cherry", 30)
print(cache.get_most_recent_key())  # Output: 'cherry'
print(cache.get_value_from_key("banana"))  # Output: 20
cache.insert_key_value_pair("date", 40)  # "apple" should be evicted
print(cache.get_value_from_key("apple"))  # Output: None
```

#### Example 3
```python
cache = LRUCache(2)
cache.insert_key_value_pair(1, 100)
cache.insert_key_value_pair(2, 200)
print(cache.get_most_recent_key())  # Output: 2
cache.get_value_from_key(1)  # Accessing key 1
print(cache.get_most_recent_key())  # Output: 1 (key 1 is now the most recent)
cache.insert_key_value_pair(3, 300)  # Evicts key 2
print(cache.get_value_from_key(2))  # Output: None
print(cache.get_value_from_key(3))  # Output: 300
```

