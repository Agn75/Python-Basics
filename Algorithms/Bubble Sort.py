# Bubble Sort
"""Bubble sort is a simple sorting algorithm that
repeatedly steps through the list, compares adjacent
 elements, and swaps them if they are in the wrong order.
  This process is repeated until the entire list is sorted."""


def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


array = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(array)
print(array)