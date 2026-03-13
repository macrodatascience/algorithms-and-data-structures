inputStr = input("Enter the nums: ")
item = int(input("Enter the item to be searched: "))
myList = [int(i) for i in inputStr.split()]
print(myList)


def binarySearch(myList:list[int], item: int):
    left = 0
    right = len(myList)-1
    foundItem = False

    while (left <= right and not foundItem):
        mid = (left+right)//2
        if myList[mid]==item:
            foundItem = True
            return foundItem
        elif myList[mid]>item:
            right = mid-1
        else:
            left = mid+1
    return foundItem


print(binarySearch(sorted(myList), item))
