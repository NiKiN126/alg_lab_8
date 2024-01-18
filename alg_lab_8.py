def count_inversions(arr):
    if arr is None or len(arr) <= 1:
        return 0

    temp = [0] * len(arr)
    return _merge_sort_and_count(arr, temp, 0, len(arr) - 1)

def _merge_sort_and_count(arr, temp, left, right):
    count = 0

    if left < right:
        mid = (left + right) // 2

        count += _merge_sort_and_count(arr, temp, left, mid)
        count += _merge_sort_and_count(arr, temp, mid + 1, right)

        count += _merge_and_count(arr, temp, left, mid, right)

    return count

def _merge_and_count(arr, temp, left, mid, right):
    i = left
    j = mid + 1
    k = left
    count = 0
    merged = []

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            k += 1
            j += 1
            count += (mid - i + 1)

    while i <= mid:
        temp[k] = arr[i]
        k += 1
        i += 1

    while j <= right:
        temp[k] = arr[j]
        k += 1
        j += 1

    for l in range(left, right + 1):
        arr[l] = temp[l]

    return count

arr = [1, 20, 6, 4, 5]
inversion_count = count_inversions(arr)
print("Количество инверсий в массиве:", inversion_count)