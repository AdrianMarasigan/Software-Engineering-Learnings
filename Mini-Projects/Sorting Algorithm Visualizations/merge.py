import matplotlib.pyplot as plt
import random

# Function to perform merge sort and visualize it with highlighted iterators


def merge_sort_visualize(arr, low, high):
    if low < high:
        mid = (low + high) // 2

        merge_sort_visualize(arr, low, mid)
        merge_sort_visualize(arr, mid + 1, high)

        merge(arr, low, mid, high)


def merge(arr, low, mid, high):
    left = arr[low:mid + 1]
    right = arr[mid + 1:high + 1]

    i = j = 0
    k = low

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

        plt.cla()
        bars = plt.bar(range(len(arr)), arr, color='salmon')
        for idx in range(low, k + 1):
            bars[idx].set_color('blue')
        # Adjust this pause duration to control the visualization speed
        plt.pause(0.5)
        for idx in range(low, k + 1):
            bars[idx].set_color('salmon')

        k += 1

    while i < len(left):
        arr[k] = left[i]
        plt.cla()
        bars = plt.bar(range(len(arr)), arr, color='salmon')
        for idx in range(low, k + 1):
            bars[idx].set_color('blue')
        # Adjust this pause duration to control the visualization speed
        plt.pause(0.5)
        for idx in range(low, k + 1):
            bars[idx].set_color('salmon')
        k += 1
        i += 1

    while j < len(right):
        arr[k] = right[j]
        plt.cla()
        bars = plt.bar(range(len(arr)), arr, color='salmon')
        for idx in range(low, k + 1):
            bars[idx].set_color('blue')
        # Adjust this pause duration to control the visualization speed
        plt.pause(0.5)
        for idx in range(low, k + 1):
            bars[idx].set_color('salmon')
        k += 1
        j += 1


# Generate a random list to sort
arr = [random.randint(1, 100) for _ in range(20)]

plt.ion()  # Enable interactive mode
plt.figure(figsize=(len(arr) / 4, 3))
# Call the merge_sort_visualize function
merge_sort_visualize(arr, 0, len(arr) - 1)

# Display the final sorted array
plt.ioff()  # Turn off interactive mode
plt.bar(range(len(arr)), arr, color='salmon')
plt.title("Sorted Array")
plt.show()
