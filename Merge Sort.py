"""
Merge Sort:
Description: Merge sort divides the input into two using recursion and sorts as it merges the outputs.
Input : [5, 4, 1, 19, 32, 25]
Output: [1, 4, 5, 19, 25, 32]
"""

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        # Recursive call on each half
        merge_sort(left)
        merge_sort(right)
        # Two iterators for traversing the two halves
        i = 0
        j = 0
        # Iterator for the main list
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        # For all the remaining values
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1





