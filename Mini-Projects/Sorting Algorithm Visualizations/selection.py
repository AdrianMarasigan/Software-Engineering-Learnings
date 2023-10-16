import matplotlib.pyplot as plt
import random
import time

# Function to perform selection sort and visualize it with highlighted iterators


def selection_sort_visualize(arr):
    n = len(arr)
    fig, ax = plt.subplots()
    ax.set_title("Selection Sort Visualization")

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

            ax.clear()
            bars = ax.bar(range(len(arr)), arr, color='salmon')
            bars[i].set_color('red')
            bars[j].set_color('blue')
            # Adjust this pause duration to control the visualization speed
            plt.pause(0.1)
            bars[i].set_color('salmon')
            bars[j].set_color('salmon')

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    # Display the final sorted array
    plt.bar(range(len(arr)), arr, color='salmon')
    plt.title("Sorted Array")
    plt.show()


# Generate a random list to sort
arr = [random.randint(1, 100) for _ in range(20)]

# Call the selection_sort_visualize function
selection_sort_visualize(arr)
