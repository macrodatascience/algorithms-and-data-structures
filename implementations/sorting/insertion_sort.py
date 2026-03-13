def insertion_sort(arr):
    print(f"Input arr: {arr}")
    
    for i in range(1, len(arr)):
        for j in range(i+1):
            if arr[j] > arr[i]:
                arr[j], arr[i] = arr[i], arr[j] 
    return arr

arr = [10, 12, 2, 102, 20, 22,91, 18, 24, -1, 200, 190, 29]
print(insertion_sort(arr))

