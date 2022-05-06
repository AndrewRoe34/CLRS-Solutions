def binary_recursive_search(arr, low, high, x):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        return binary_recursive_search(arr, low, mid - 1, x)
    else:
        return binary_recursive_search(arr, mid + 1, high, x)    

    
def binary_iterative_search(arr, low, high, x):
    while len(arr) > 0 and low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
    return -1


arr = [1, 2, 3, 4, 5]

print(binary_recursive_search(arr, 0, len(arr) - 1, 2))
print(binary_iterative_search(arr, 0, len(arr) - 1, 4))
