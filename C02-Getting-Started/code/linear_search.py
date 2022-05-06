def linear_search(arr, x):
    for i in range(arr):
        if arr[i] == x:
            return i
    return -1


arr = [1, 2, 3, 4, 5]
print(linear_search(arr, 4))