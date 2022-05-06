def merge_sort_inversions(arr):
    if len(arr) == 1:
        return 0

    mid = len(arr) // 2

    arr_a = arr[:mid]
    arr_b = arr[mid:]

    inversions = merge_sort_inversions(arr_a) + merge_sort_inversions(arr_b)

    a_count = 0
    b_count = 0
    for i in range(len(arr)):
        if b_count >= len(arr_b) or a_count < len(arr_a) and arr_a[a_count] < arr_b[b_count]:
            arr[i] = arr_a[a_count]
            a_count = a_count + 1
        else:
            arr[i] = arr_b[b_count]
            b_count = b_count + 1
            inversions = (len(arr_a) - a_count) + inversions
    return inversions


arr = [5, 2, 1, 4, 3]
print(merge_sort_inversions(arr))