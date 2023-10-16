import matplotlib.pyplot as plt
import random
import time

# Function to perform bubble sort and visualize it with highlighted iterators


def bubble_sort_visualize(arr):
    n = len(arr)
    fig, ax = plt.subplots()
    ax.set_title("Bubble Sort Visualization")

    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

            ax.clear()
            bars = ax.bar(range(len(arr)), arr, color='salmon')
            bars[j].set_color('red')
            bars[j+1].set_color('blue')
            plt.pause(0.5)
            bars[j].set_color('salmon')
            bars[j+1].set_color('salmon')

        if not swapped:
            break


# Generate a random list to sort
arr = [random.randint(1, 100) for _ in range(20)]

# Call the bubble_sort_visualize function
bubble_sort_visualize(arr)

# Display the final sorted array
plt.bar(range(len(arr)), arr, color='salmon')
plt.title("Sorted Array")
plt.show()
