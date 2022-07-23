import sys

#assume array is sorted, perform binary search
def findfirst(array, target):
    head, tail = 0, len(array) - 1
    while head <= tail:
        mid = (tail + head) // 2
        if array[mid] == target and (mid == 0 or array[mid - 1] < target):
            return mid
        elif array[mid] < target:
            head = mid + 1
        elif array[mid] >= target:
            tail = mid - 1
    return None

def findlast(array, target):
    head, tail = 0, len(array) - 1
    while head <= tail:
        mid = (tail + head) // 2
        if array[mid] == target and (mid == len(array) - 1 or array[mid + 1] > target):
            return mid
        elif array[mid] <= target:
            head = mid + 1
        elif array[mid] > target:
            tail = mid - 1
    return None

input = sys.stdin.readline

n = int(input())
boxToSearch = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

arr = sorted(boxToSearch)
result = []
for n in nums:
    a, b = findfirst(arr, n), findlast(arr, n)
    if a == None:
        result.append(0)
    else:
        result.append(b - a + 1)

print(*result)