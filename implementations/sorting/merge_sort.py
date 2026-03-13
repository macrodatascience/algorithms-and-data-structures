def merge_sort(nums):

    if len(nums)<=1:
        return nums

    middle = len(nums)//2

    left_arr = nums[:middle]
    right_arr = nums[middle:]

    left_sorted = merge_sort(left_arr)
    right_sorted = merge_sort(right_arr)

    return merge(left_sorted, right_sorted)

def merge(left, right):

    i = 0
    j = 0
    
    merged = []

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

if __name__ == "__main__":
    print(merge_sort([40,30,50,60,45,15,25]))

    print(merge_sort([4,30,0,6,15,25,35]))
    print(merge_sort([40,30,50,60,95,45,95]))
    print(merge_sort([4000,300,150,600,455,555,25]))



