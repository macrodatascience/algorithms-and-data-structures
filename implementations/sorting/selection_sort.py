def selection_sort(arr):
    print(f"Input array: {arr}")
    for i in range(len(arr)):
        smallest = i
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j

        arr[i], arr[smallest] = arr[smallest], arr[i] 
    return arr

arr = [10, 12, 20, 15, 13, 16, 19, 25]
print(selection_sort(arr))
