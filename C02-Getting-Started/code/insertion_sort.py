def insertion_sort(arr):
    for i in range(1, len(arr)):
        k = arr[i]
        j = i - 1
        while j >= 0 and k > arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = k


arr = [5, 4, 3, 2, 1]
insertion_sort(arr)
print(arr)
