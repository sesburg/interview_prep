import sys


#assume array is sorted, perform binary search
def binary_search(array, target):
    head, tail = 0, len(array) - 1
    while head <= tail:
        mid = (tail + head) // 2
        if array[mid] == target:
            return 1
        elif array[mid] < target:
            head = mid + 1
        elif array[mid] > target:
            tail = mid - 1
    return 0

input = sys.stdin.readline

n = int(input())
boxToSearch = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

boxToSearch = sorted(boxToSearch)
for i in nums:
    print(binary_search(boxToSearch, i))

