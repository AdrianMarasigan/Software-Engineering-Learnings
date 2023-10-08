# Algorithms

# Table of Contents
- [Big O Notation](#big-o-notation)
- [Sorting](#sorting)
- [Searching](#searching)
- [Strings](#strings)

## Big O Notation
Big O Notation is a mathematical notation used in computer science and algorithm analysis to describe the upper bound or worst-case time complexity of an algorithm. It provides a way to classify algorithms based on how their execution time grows in relation to the size of the input data. Understanding Big O Notation is crucial for evaluating algorithm efficiency and making informed decisions when choosing algorithms for specific tasks.

Big O Notation expresses the time complexity of an algorithm as a function of the input size (typically denoted as "n"). It allows us to answer questions like "How does the execution time of an algorithm scale as the input size increases?" By analyzing the Big O complexity of an algorithm, we can make informed decisions about which algorithm to choose for a particular problem.

### Common Notations
- O(1) - Constant Time Complexity: Algorithms with constant time complexity execute in the same amount of time regardless of the input size. They have a fixed number of operations.

- O(log n) - Logarithmic Time Complexity: Algorithms with logarithmic time complexity reduce the problem size by a constant factor in each step. They are efficient for large datasets.

- O(n) - Linear Time Complexity: Algorithms with linear time complexity have their execution time grow proportionally with the size of the input. Doubling the input size roughly doubles the execution time.

- O(n log n) - Linearithmic Time Complexity: Algorithms with linearithmic time complexity combine linear and logarithmic growth. They are efficient for many sorting and divide-and-conquer algorithms.

- O(n^2) - Quadratic Time Complexity: Algorithms with quadratic time complexity have their execution time grow with the square of the input size. They are less efficient and may become impractical for large inputs.

- O(n^k) - Polynomial Time Complexity: Algorithms with polynomial time complexity have their execution time grow with a power of the input size. The value of "k" determines the degree of the polynomial.

- O(2^n) - Exponential Time Complexity: Algorithms with exponential time complexity have execution times that grow exponentially with the input size. They are highly inefficient and impractical for large inputs.

## Sorting
Sorting is a fundamental operation in computer science and data processing. It involves arranging a collection of items or data elements in a specific order, typically in ascending or descending order. Sorting is a key step in various algorithms and applications, including searching, data analysis, and database management. This section explores different sorting algorithms, their characteristics, and their use cases.


### Bubble Sort
Bubble Sort is a simple comparison-based sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, indicating that the list is sorted. Bubble Sort is easy to understand but not very efficient, especially for large lists.

#### Key Characteristics
1. Comparison-Based: Bubble Sort compares adjacent elements in the list and swaps them if they are out of order. This comparison and swapping process continues until the entire list is sorted.
2. In-Place Sorting: Bubble Sort operates on the original list and does not require additional memory for temporary data structures. It is an in-place sorting algorithm.
3. Stable Sorting: Bubble Sort is a stable sorting algorithm, meaning it maintains the relative order of equal elements. If two elements have the same value, their original order will be preserved in the sorted list.
4. Time Complexity: Bubble Sort has a worst-case and average-case time complexity of O(n^2), making it inefficient for large datasets. However, it has a best-case time complexity of O(n), which occurs when the list is already sorted.

Use Case: Bubble Sort is rarely used in practice due to its inefficiency for large datasets. It may be suitable for small lists or as a teaching example to illustrate sorting concepts.

Below is a Python implementation of bubble sort:

```Python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to optimize the algorithm by checking if any swaps are made in a pass
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap the elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no swaps were made in a pass, the list is already sorted
        if not swapped:
            break
```

### Selection Sort
Selection Sort is a simple comparison-based sorting algorithm that divides the input list into two parts: the sorted portion and the unsorted portion. It repeatedly selects the smallest (or largest, depending on the desired order) element from the unsorted portion and moves it to the end of the sorted portion. Selection Sort is straightforward to implement but not very efficient for large lists.

#### Key Characteristics
1. Comparison-Based: Selection Sort selects the smallest (or largest) element by comparing elements in the unsorted portion of the list and moving the selected element to its correct position in the sorted portion.
2. In-Place Sorting: Selection Sort is an in-place sorting algorithm, as it sorts the original list without requiring additional memory for temporary data structures.
3. Not Stable: Selection Sort is not a stable sorting algorithm. It may change the relative order of equal elements.
4. Time Complexity: Selection Sort has a consistent time complexity of O(n^2), regardless of the input data. It is inefficient for large datasets but may perform better than Bubble Sort in some cases.

Use Cases: Selection Sort, like Bubble Sort, is not commonly used for large datasets. It can be suitable for small lists or as a simple sorting algorithm when stability is not a concern.

Below is a Python implementation of selection sort.
```Python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the smallest element with the current position
        arr[i], arr[min_index] = arr[min_index], arr[i]
```

### Insertion Sort
Insertion Sort is a simple comparison-based sorting algorithm that builds the final sorted list one element at a time. It takes each element from the unsorted portion of the list and inserts it into its correct position within the sorted portion. Insertion Sort is efficient for small datasets and is often used for partially sorted lists.

#### Key Characteristics
1. Comparison-Based: Insertion Sort compares each element with the elements in the sorted portion of the list and inserts it into the correct position.
2. In-Place Sorting: Insertion Sort is an in-place sorting algorithm, as it sorts the original list without requiring additional memory for temporary data structures.
3. Stable Sorting: Insertion Sort is a stable sorting algorithm, preserving the relative order of equal elements.
4. Time Complexity: The time complexity of Insertion Sort is O(n^2) in the worst and average cases. However, it can perform well for small datasets and lists that are already partially sorted, where its time complexity can be closer to O(n).

Use Cases: Insertion Sort is suitable for small lists or lists with only a few elements out of order. It is often used as a building block in more advanced sorting algorithms.

```Python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
```

### Merge Sort
Merge Sort is a divide-and-conquer sorting algorithm that recursively divides the input list into smaller sublists, sorts them, and then merges them back together to produce a sorted list. Merge Sort is known for its stability and consistent O(n log n) time complexity, making it efficient for large datasets.

#### Key Characteristics
1. Divide and Conquer: Merge Sort divides the input list into smaller sublists, sorts them independently, and then merges them back together to create a sorted list. This divide-and-conquer approach leads to its efficiency.
2. Stable Sorting: Merge Sort is a stable sorting algorithm, preserving the relative order of equal elements.
3. Efficient Time Complexity: Merge Sort has a time complexity of O(n log n) in the worst, average, and best cases, making it suitable for sorting large datasets.

Use Cases: Merge Sort is commonly used when a stable, efficient, and predictable sorting algorithm is needed, especially for large datasets. It is often used as the basis for external sorting algorithms.

Below in a Python implementation of Merge sort.
```Python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
```

### Quick Sort
Quick Sort is a divide-and-conquer sorting algorithm that selects a "pivot" element from the input list and partitions the list into two sublists: elements less than the pivot and elements greater than the pivot. It then recursively sorts the sublists. Quick Sort is known for its efficiency and is often used in practice.

#### Key Characteristics
1. Divide and Conquer: Quick Sort selects a pivot element, divides the list into smaller sublists, and sorts them independently. This divide-and-conquer approach contributes to its efficiency.
2. In-Place Sorting: Quick Sort can be implemented as an in-place sorting algorithm, which means it sorts the original list without requiring additional memory for temporary data structures. However, some implementations may use additional memory for stability.
3. Not Always Stable: Quick Sort is not a stable sorting algorithm. It may change the relative order of equal elements.
4. Efficient Time Complexity: Quick Sort has an average and best-case time complexity of O(n log n), making it highly efficient for large datasets. However, in the worst case, it can be O(n^2) if poorly chosen pivot elements cause unbalanced partitions.

Use Cases: Quick Sort is widely used for its efficiency and is the default sorting algorithm in many programming languages and libraries. It is suitable for sorting large datasets in-memory and out-of-memory.

Below is a Python implementation of quick sort:

```Python
def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high

    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while arr[right] >= pivot and right >= left:
            right -= 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right
```

### Heap Sort
Heap Sort is a comparison-based sorting algorithm that leverages the properties of a binary heap data structure. It builds a max-heap (for ascending order) or a min-heap (for descending order) from the input list and repeatedly removes the root element (the maximum or minimum, depending on the heap type) to build the sorted list. Heap Sort is efficient and can achieve a consistent O(n log n) time complexity.

#### Key Characteristics
1. Heap Data Structure: Heap Sort relies on a binary heap data structure, which is a binary tree with specific properties (max-heap or min-heap). It uses the heap to efficiently find the maximum (for ascending order) or minimum (for descending order) element in the list.
2. In-Place Sorting: Heap Sort can be implemented as an in-place sorting algorithm, meaning it sorts the original list without requiring additional memory for temporary data structures.
3. Not Always Stable: Heap Sort is not a stable sorting algorithm. It may change the relative order of equal elements.
4. Efficient Time Complexity: Heap Sort has an average and worst-case time complexity of O(n log n), making it efficient for large datasets.

Use Cases: Heap Sort is often used when a stable sorting algorithm is not required, and efficiency is crucial. It is suitable for sorting large datasets and is used in various applications, including priority queues and scheduling algorithms.

```Python
def heap_sort(arr):
    n = len(arr)

    # Build a max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap root (max element) with the last element
        heapify(arr, i, 0)

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)
```

## Searching
Searching algorithms are essential in computer science and data processing to locate specific elements within a data structure, such as an array or list. These algorithms are designed to efficiently find the target element(s) within the data, and their choice depends on factors like data structure properties, data ordering, and efficiency requirements. This section explores different searching algorithms, their characteristics, and use cases.

### Linear Search
Linear Search, also known as Sequential Search, is a straightforward searching algorithm that iterates through the entire dataset from start to finish, checking each element one by one until the target element is found or the entire dataset has been scanned. It is suitable for unordered data but can be inefficient for large datasets.

#### Key Characteristics
1. Linear Time Complexity: Linear Search has a time complexity of O(n) in the worst-case scenario, where "n" is the size of the dataset. This means the algorithm's time requirements grow linearly with the dataset size.
2. Simple Implementation: Linear Search is easy to implement and does not require the data to be sorted. It is useful when the dataset lacks any specific ordering.

Use Cases: Linear Search is suitable for small datasets or scenarios where data is not ordered or indexed. It is also commonly used for searching in linked lists.

```Python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

### Binary Search
Binary Search is a more efficient searching algorithm designed for ordered datasets. It repeatedly divides the dataset in half and compares the middle element with the target value. If the target is smaller, the algorithm continues searching in the lower half; if the target is larger, it searches in the upper half. Binary Search quickly narrows down the search space and is highly efficient for large ordered datasets.

#### Key Characteristics
1. Logarithmic Time Complexity: Binary Search has a time complexity of O(log n) in the worst-case scenario. It effectively reduces the search space by half in each step, making it suitable for large datasets.
2. Ordered Data Requirement: Binary Search requires the data to be sorted in ascending or descending order to work correctly. This requirement ensures that the algorithm can eliminate half of the remaining elements in each step.

Use Cases: Binary Search is ideal for searching in sorted arrays or lists. It is commonly used in searching applications and is a fundamental algorithm in computer science.

```Python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```


## Strings
String algorithms are specialized algorithms used for processing and manipulating strings, which are sequences of characters. These algorithms are crucial in various applications, such as text processing, pattern matching, and data parsing. This section explores different string algorithms, their characteristics, and use cases.

### Knuth-Morris-Pratt (KMP) Algorithm
The Knuth-Morris-Pratt (KMP) Algorithm is used for substring searching within a longer string. It efficiently finds all occurrences of a substring by avoiding unnecessary character comparisons.

#### Key Characteristics
1. Efficiency: The KMP Algorithm achieves a time complexity of O(n + m), where "n" is the length of the text and "m" is the length of the substring to be searched.
2. Partial Match Table: KMP uses a precomputed partial match table to skip comparisons when a mismatch occurs. This enhances its efficiency.

Use Cases: KMP is suitable for searching substrings within texts, including applications like text editors, search engines, and string pattern matching.

```Python
def build_partial_match_table(pattern):
    table = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        table[i] = j
    return table

def kmp_search(text, pattern):
    partial_match_table = build_partial_match_table(pattern)
    matches = []
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = partial_match_table[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            matches.append(i - j + 1)
            j = partial_match_table[j - 1]
    return matches
```

### Boyer-Moore Algorithm
The Boyer-Moore Algorithm is another efficient substring searching algorithm. It uses a "bad character" and "good suffix" rule to skip unnecessary comparisons.

#### Key Characteristics
1. Efficiency: The Boyer-Moore Algorithm achieves a time complexity of O(n + m) in practice. It is known for its speed in practical applications.
2. Heuristic Rules: Boyer-Moore uses heuristic rules to skip comparisons based on the last occurrence of characters in the substring and the text.

Use Cases: Boyer-Moore is widely used for searching substrings in text processing, including searching in large documents and string matching.

```Python
def build_bad_character_table(pattern):
    table = {}
    for i in range(len(pattern) - 1):
        table[pattern[i]] = len(pattern) - 1 - i
    return table

def build_good_suffix_table(pattern):
    m = len(pattern)
    suffix_table = [-1] * m
    j = 0
    for i in range(m - 1, -1, -1):
        if is_suffix(pattern, i + 1):
            j = m - 1 - i
        suffix_table[i] = j
    return suffix_table

def is_suffix(pattern, p):
    j = len(pattern) - 1
    for i in range(p, -1, -1):
        if pattern[i] != pattern[j]:
            return False
        j -= 1
    return True

def boyer_moore_search(text, pattern):
    bad_character_table = build_bad_character_table(pattern)
    good_suffix_table = build_good_suffix_table(pattern)
    matches = []
    i = 0
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j < 0:
            matches.append(i)
            i += good_suffix_table[0]
        else:
            i += max(bad_character_table.get(text[i + j], 0), good_suffix_table[j])
    return matches
```

### String Reversal
String reversal is a common string manipulation task that involves reversing the order of characters in a string.

#### Key Characteristics
1. Efficiency: String reversal can be achieved with a time complexity of O(n), where "n" is the length of the string.
2. In-Place vs. Out-of-Place: String reversal can be done in-place (modifying the original string) or out-of-place (creating a new reversed string).

Use Cases: String reversal is useful in various applications, including text processing, cryptography, and data transformation.

```Python
def reverse_string(input_string):
    return input_string[::-1]
```

### String Concatenation
String concatenation involves combining two or more strings into a single string.

#### Key Characteristics
1. Efficiency: The time complexity of string concatenation depends on the implementation. In most cases, it is O(n), where "n" is the total length of the strings being concatenated.
2. In-Place vs. Out-of-Place: Some string concatenation methods modify the original string (in-place), while others create a new string (out-of-place).

Use Cases: String concatenation is essential for building longer strings from smaller components, such as in text generation, logging, and data serialization.

```Python
def concatenate_strings(strings):
    return ''.join(strings)

# Example usage
string_list = ['abc', 'def']
result = concatenate_strings(string_list)
print(result)  # Output: 'abcdef'
```

```Python
s = 'abc'
t = 'def'
result = s + t
print(result)  # Output: 'abcdef'
```

### Regular Expressions
Regular expressions (regex) are a powerful tool for string matching and pattern recognition. They allow you to define search patterns and perform complex string manipulations.

#### Key Characteristics
1. Versatility: Regular expressions support a wide range of string matching and manipulation tasks, from simple substring searches to complex pattern extractions.
2. Pattern Language: Regular expressions use a pattern language to specify search patterns, making them highly flexible.
3. Efficiency: The efficiency of regular expressions can vary based on the complexity of the pattern. Simple patterns can be matched quickly, but complex patterns may require more processing time.

Use Cases: Regular expressions are used in text processing, data validation, web scraping, and many other applications that involve string matching.

```Python
import re

# Example of using regular expressions
text = "Hello, my email is example@email.com"
pattern = r'\S+@\S+'
matches = re.findall(pattern, text)
print(matches)  # Output: ['example@email.com']
```

### Rabin-Karp Algorithm
The Rabin-Karp Algorithm is a string matching algorithm that uses hashing to find occurrences of a pattern in a text efficiently.

#### Key Characteristics
1. Efficiency: Rabin-Karp has an average-case time complexity of O(n + m), where "n" is the length of the text and "m" is the length of the pattern. It is particularly efficient for large texts and patterns.
2. Hashing: Rabin-Karp uses rolling hashing to compute hash values for the text and the pattern. This allows for quick comparisons and shifts.

Use Cases: Rabin-Karp is used for pattern matching in text processing, plagiarism detection, and substring searching.

```Python
def rabin_karp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    pattern_hash = hash(pattern)
    text_hash = hash(text[:m])
    matches = []

    for i in range(n - m + 1):
        if text_hash == pattern_hash and text[i:i + m] == pattern:
            matches.append(i)
        if i < n - m:
            text_hash = (text_hash - ord(text[i])) // 256 + ord(text[i + m]) * (256 ** (m - 1))

    return matches
```
