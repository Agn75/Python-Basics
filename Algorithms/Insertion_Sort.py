"""
In the insertion_sort function,  we iterate over the array starting
from the second element (index 1). or each element, we compare it with the elements
 on its left side and shift them to the right until
 we find the correct position for the current element.
 Finally, we insert the element in its correct position.
"""


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage:
array = [9, 5, 1, 4, 3]
insertion_sort(array)
print(array)