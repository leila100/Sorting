# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    merged_arr = []
    # TO-DO
    i = 0
    j = 0

    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr.append(arrA[i])
            i += 1
        else:
            merged_arr.append(arrB[j])
            j += 1
    if i >= len(arrA):
        if(len(arrB) != 0):
            merged_arr.append(*arrB[j:])
    elif j >= len(arrB):
        if(len(arrA) != 0):
            merged_arr.append(*arrA[i:])
    return merged_arr


# arr1 = [1, 5, 8, 10]
arr1 = [1, 5]
# arr2 = [0, 4, 7, 9]
arr2 = [0, 4]
print(merge(arr1, arr2))

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
