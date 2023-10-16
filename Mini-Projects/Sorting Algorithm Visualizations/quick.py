import matplotlib.pyplot as plt
import random

# Function to perform quick sort and visualize it with highlighted pivot and partitions


def quick_sort_visualize(arr, low, high):
    if low < high:
        pivot_idx = partition(arr, low, high)
        quick_sort_visualize(arr, low, pivot_idx - 1)
        quick_sort_visualize(arr, pivot_idx + 1, high)


def partition(arr, low, high):
    # Choose the pivot element (you can customize the pivot selection)
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

        plt.cla()
        bars = plt.bar(range(len(arr)), arr, color='salmon')
        bars[high].set_color('orange')  # Highlight the pivot
        for idx in range(low, i + 1):
            bars[idx].set_color('blue')
        for idx in range(i + 1, j):
            bars[idx].set_color('green')
        # Adjust this pause duration to control the visualization speed
        plt.pause(0.25)

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    plt.cla()
    bars = plt.bar(range(len(arr)), arr, color='salmon')
    for idx in range(low, i + 1):
        bars[idx].set_color('blue')
    for idx in range(i + 1, high):
        bars[idx].set_color('green')
    # Adjust this pause duration to control the visualization speed
    plt.pause(0.5)

    return i + 1


# Generate a random list to sort
arr = [random.randint(1, 100) for _ in range(20)]

plt.ion()  # Enable interactive mode
plt.figure(figsize=(len(arr) / 4, 3))
# Call the quick_sort_visualize function with your own list and range (if needed)
quick_sort_visualize(arr, 0, len(arr) - 1)

# Display the final sorted array
plt.ioff()  # Turn off interactive mode
plt.bar(range(len(arr)), arr, color='salmon')
plt.title("Sorted Array")
plt.show()
