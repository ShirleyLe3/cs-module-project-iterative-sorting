def linear_search(arr, target):
    if len(arr) > 0:
        for i, num in enumerate(arr):
            if num == target:
                return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    if len(arr) > 0:
        left = 0
        right = len(arr) - 1
        while right >= left:
            middle = (left + right) // 2
            if target == arr[middle]:
                return middle
            elif target < arr[middle]:
                right = middle - 1
            else:
                left = middle + 1
    return -1  # not found
