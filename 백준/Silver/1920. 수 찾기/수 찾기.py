import sys
def binary_search(arr, target):
    start, end = 0, len(arr)-1
    
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == target:
            return 1
        elif target < arr[mid]:
            end = mid - 1
        elif target > arr[mid]:
            start = mid + 1
    return 0

n = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))
arr1.sort()
m = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    print(binary_search(arr1, arr2[i]))