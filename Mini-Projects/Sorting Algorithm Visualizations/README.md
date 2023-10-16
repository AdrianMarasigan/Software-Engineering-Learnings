# Sorting Algorithm Visualizations
These Python scripts demonstrates how some sorting algorithms work with a visual representation of the sorting process using the matplotlib library. 

1. Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted.
2. Selection Sort is a straightforward sorting algorithm that divides the input list into two parts: the sorted and unsorted sublists. It repeatedly finds the minimum (or maximum) element from the unsorted sublist and swaps it with the first element of the unsorted sublist. This process continues until the entire list is sorted. Selection Sort is not very efficient for large lists but is easy to understand and implement due to its simplicity.
3. Merge Sort is a divide-and-conquer sorting algorithm that divides the unsorted list into smaller sublists, sorts them, and then merges these sorted sublists to produce a single sorted list. It is known for its stability and guarantees consistent performance, making it a popular choice for sorting large datasets. Merge Sort is a balanced algorithm that has a time complexity of O(n log n) and is often used in external sorting scenarios.
4. Quick Sort is a highly efficient and widely used sorting algorithm. It employs a divide-and-conquer strategy, where it selects a 'pivot' element and rearranges the list so that elements smaller than the pivot are on its left, and elements greater are on its right. This process is recursively applied to the sublists on both sides of the pivot until the entire list is sorted. Quick Sort's performance can be exceptional, making it one of the fastest sorting algorithms in practice.

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

## Customization
You can customize the script by modifying the following aspects:

arr: You can change the arr variable to contain any list of integers you want to sort.
plt.pause(0.5): You can adjust the pause duration to control the speed of the visualization. Smaller values will make the sorting process faster, while larger values will slow it down.