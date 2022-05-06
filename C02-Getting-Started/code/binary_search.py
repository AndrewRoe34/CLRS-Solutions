def binary_search(arr, low, high, x):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        return binary_search(arr, low, mid - 1, x)
    else:
        return binary_search(arr, mid + 1, high, x)


arr = [1, 2, 3, 4, 5]

print(binary_search(arr, 0, len(arr) - 1, 2))
