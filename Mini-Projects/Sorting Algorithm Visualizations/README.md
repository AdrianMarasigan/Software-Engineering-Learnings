# Sorting Algorithm Visualizations
These Python scripts demonstrates how some sorting algorithms work with a visual representation of the sorting process using the matplotlib library. 

The most challenging part of this project was finding out how to best visualize each algorithm for understanding. Please feel free to use my code and play around with the different visualiation options, which is a fun way for developing an understadning of the algorithm at each step and for practicing your implementation of each algorithm.

### Bubble Sort 
Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted.

![Bubble Sort](https://github.com/c0olade/Software-Engineering-Journey/blob/main/Mini-Projects/Sorting%20Algorithm%20Visualizations/images/bubble%20sort.gif)

### Selection Sort 
Selection Sort is a straightforward sorting algorithm that divides the input list into two parts: the sorted and unsorted sublists. It repeatedly finds the minimum (or maximum) element from the unsorted sublist and swaps it with the first element of the unsorted sublist. This process continues until the entire list is sorted. Selection Sort is not very efficient for large lists but is easy to understand and implement due to its simplicity.

![Selection Sort](https://github.com/c0olade/Software-Engineering-Journey/blob/main/Mini-Projects/Sorting%20Algorithm%20Visualizations/images/selection.gif)

### Merge Sort
Merge Sort is a divide-and-conquer sorting algorithm that divides the unsorted list into smaller sublists, sorts them, and then merges these sorted sublists to produce a single sorted list. It is known for its stability and guarantees consistent performance, making it a popular choice for sorting large datasets. Merge Sort is a balanced algorithm that has a time complexity of O(n log n) and is often used in external sorting scenarios.

![Merge Sort](https://github.com/c0olade/Software-Engineering-Journey/blob/main/Mini-Projects/Sorting%20Algorithm%20Visualizations/images/merge.gif)

### Quick Sort 
Quick Sort is a highly efficient and widely used sorting algorithm. It employs a divide-and-conquer strategy, where it selects a 'pivot' element and rearranges the list so that elements smaller than the pivot are on its left, and elements greater are on its right. This process is recursively applied to the sublists on both sides of the pivot until the entire list is sorted. Quick Sort's performance can be exceptional, making it one of the fastest sorting algorithms in practice.

![Quick Sort](https://github.com/c0olade/Software-Engineering-Journey/blob/main/Mini-Projects/Sorting%20Algorithm%20Visualizations/images/quick.gif)

## Prerequisites
Before running this code, you need to have Python installed on your system. You will also need to install the matplotlib library if you haven't already. You can install it using pip:

```bash
pip install matplotlib
```
## How to Run
### Clone the Repository
If you haven't already, clone this repository to your local machine. You can do this using Git:

```bash
git clone https://github.com/your-username/your-repo.git
```

### Navigate to the Directory
Go to the directory where you saved the script using the cd command:
```bash
cd your-repo
```

### Run the Script
Run the Python script using your Python interpreter. For example:

```bash
python bubble_sort_visualization.py
```

### Close the Visualization:
After the sorting is complete and you've observed the visualization, you can close the visualization window to end the program.
