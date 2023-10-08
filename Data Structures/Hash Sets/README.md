# Hash Sets
A hash set is a collection of unique values, where each value is hashed to a unique location within the set. Hash sets are commonly used when you need to check for the presence of an element or store a collection of distinct elements efficiently.

## Key Characteristics
1. Uniqueness: Hash sets contain only unique elements. Duplicates are automatically eliminated.

```Python
# Creating a hash set with unique elements
unique_set = set()

# Adding elements to the set (duplicates are automatically eliminated)
unique_set.add(10)
unique_set.add(20)
unique_set.add(10)  # Duplicate element, not added

print(unique_set)  # Output: {10, 20}
```

2. Hashing: Elements are hashed to determine their storage location within the set. A good hash function minimizes collisions, where different elements map to the same location.

```Python
# Custom hash function for integers
def custom_hash(x):
    return x % 5  # Example hash function

# Creating a hash set with a custom hash function
hash_set = set()

# Adding elements to the set (hashing determines storage location)
hash_set.add(10)  # Hashes to 0
hash_set.add(20)  # Hashes to 0 (collision)
hash_set.add(30)  # Hashes to 1

print(hash_set)  # Output: {10, 30, 20}
```

3. Constant-Time Operations: On average, hash sets provide constant-time (O(1)) operations for insertion, deletion, and lookup.
```Python
# Creating a hash set
my_set = set()

# Insertion (constant-time average)
my_set.add(10)
my_set.add(20)

# Lookup (constant-time average)
element_exists = 10 in my_set  # True

# Deletion (constant-time average)
my_set.remove(20)

print(my_set)         # Output: {10}
print(element_exists)  # Output: True
```

4. Dynamic Sizing: Hash sets can dynamically resize to accommodate more elements efficiently.

```Python
# Creating a hash set with elements
my_set = set([10, 20, 30])

# Inserting elements (dynamic resizing)
my_set.add(40)  # Resizing may occur here if the load factor threshold is reached

print(my_set)  # Output: {10, 20, 30, 40}
```


## Use Cases
- Checking for the presence of an element in a large collection (e.g., membership test).
- Removing duplicates from a list or collection of data.
- Efficiently storing a collection of unique values without manual checks for uniqueness.