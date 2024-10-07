def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iterations = 0
    saved_high = None

    while low <= high:
        iterations += 1
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            saved_high = arr[mid]
            high = mid - 1
        else:
            return (iterations,  arr[mid])
    return (iterations, saved_high)

arr = [0.5, 1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]
print(binary_search(arr, 0))
print(binary_search(arr, 1))
print(binary_search(arr, 1.1))
print(binary_search(arr, 5.5))
print(binary_search(arr, 9.9))
print(binary_search(arr, 11))