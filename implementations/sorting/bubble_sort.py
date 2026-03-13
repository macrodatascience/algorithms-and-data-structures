def bubble_sort(arr):
    print(f"input array: {arr}")
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] 


    return arr 

arr = [10, 12, 8, 7, 4, 20, 24, 11]

print(bubble_sort(arr))
