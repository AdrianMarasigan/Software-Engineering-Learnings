# Hash Maps (Hash Tables)
A hash map, also known as a hash table, is a data structure that associates keys with values. Each key is hashed to determine its storage location, and the associated value is stored at that location. Hash maps are widely used for efficient data retrieval and storage, with keys serving as unique identifiers.

## Key Characteristics
1. Key-Value Pairs: Hash maps store data as key-value pairs, where each key is associated with a specific value.

```Python
# Creating a hash map with key-value pairs
my_dict = {}

# Adding key-value pairs to the hash map
my_dict['apple'] = 5
my_dict['banana'] = 3
my_dict['cherry'] = 8

print(my_dict)  # Output: {'apple': 5, 'banana': 3, 'cherry': 8}
```

2. Hashing: Similar to hash sets, hash maps use hashing to determine the storage location of keys and values.

```Python
# Custom hash function for strings
def custom_hash(key):
    hash_value = 0
    for char in key:
        hash_value += ord(char)  # Sum of ASCII values of characters
    return hash_value

# Creating a hash map with a custom hash function
custom_map = {}

# Adding key-value pairs (hashing determines storage location)
custom_map['cat'] = 'meow'  # Hashes to 314
custom_map['dog'] = 'woof'  # Hashes to 316

print(custom_map)  # Output: {'cat': 'meow', 'dog': 'woof'}
```

3. Constant-Time Operations: On average, hash maps provide constant-time (O(1)) operations for insertion, deletion, and lookup based on keys.

```Python
# Creating a hash map
my_dict = {'apple': 5, 'banana': 3, 'cherry': 8}

# Lookup (constant-time average)
value = my_dict['banana']  # Retrieving the value associated with 'banana'

# Insertion (constant-time average)
my_dict['date'] = 6  # Adding a new key-value pair

# Deletion (constant-time average)
del my_dict['apple']  # Removing the 'apple' key-value pair

print(my_dict)  # Output: {'banana': 3, 'cherry': 8, 'date': 6}
```

4. Dynamic Sizing: Hash maps can dynamically resize to accommodate more key-value pairs efficiently.

```Python
# Creating a hash map with elements
my_dict = {'apple': 5, 'banana': 3, 'cherry': 8}

# Inserting elements (dynamic resizing)
my_dict['date'] = 6  # Resizing may occur here if the load factor threshold is reached

print(my_dict)  # Output: {'apple': 5, 'banana': 3, 'cherry': 8, 'date': 6}
```

Python's built-in dictionary (dict) handles the details of hashing, collision resolution, and resizing, making it easy to work with hash maps while benefiting from the characteristics mentioned above.

## Use Cases
- Implementing data caches, such as in-memory caching of database query results.
- Efficiently looking up values associated with specific keys, as in dictionaries.
- Storing and retrieving key-value pairs for rapid access to data.