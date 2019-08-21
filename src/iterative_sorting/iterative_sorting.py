import random

# TO-DO: Complete the selection_sort() function below


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                swapped = True

    return arr

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):
    counts = []
    output = []
    if len(arr) == 0:
        return arr
    if maximum == -1:
        maximum = max(arr)
    for i in range(0, maximum+1):
        counts.append(0)
    for i in range(0, len(arr)):
        if arr[i] < 0:
            return "Error, negative numbers not allowed in Count Sort"
        counts[arr[i]] += 1
    for i in range(0, len(counts)):
        if counts[i] != 0:
            for j in range(0, counts[i]):
                output.append(i)
    return output
