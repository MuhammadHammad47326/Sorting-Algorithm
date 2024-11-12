import time
import random

# Sorting Algorithms

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        merge_sort(left)
        merge_sort(right)
        
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Function to measure execution time
def measure_time(sort_func, array):
    start_time = time.time()
    sort_func(array)
    return time.time() - start_time

# Array configurations
size = 1000  # size of each array

# Array 1: Best Case (already sorted)
array1 = list(range(size))

# Array 2: Average Case (random order)
array2 = random.sample(range(size), size)

# Array 3: Worst Case (reverse sorted)
array3 = list(range(size, 0, -1))

# Perform sorting and measure time
results = {
    'Bubble Sort': [],
    'Selection Sort': [],
    'Merge Sort': [],
    'Quick Sort': []
}

for sort_name, sort_func in zip(results.keys(), [bubble_sort, selection_sort, merge_sort, quick_sort]):
    # Copy arrays to avoid in-place sorting side effects
    for array in [array1, array2, array3]:
        arr_copy = array.copy()  # copy of the array to sort
        exec_time = measure_time(sort_func, arr_copy)
        results[sort_name].append(exec_time)

results
