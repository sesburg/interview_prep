import sys

''' This was too slow
from bisect import bisect_right
def placeRouter(arr, space):
    last = arr[0]
    count = 1
    while True:
        val = last + space
        idx = bisect_right(arr, val)
        if val > arr[-1] or idx >= len(arr):
            break
        elif val == arr[idx - 1]:
            last = val
            count += 1
        else:
            last = arr[idx]
            count += 1
    return count
'''     
def binary_search(arr, target):
    start, end, n = arr[0], arr[-1], len(arr)
    head, tail = 1, (end - start)
    best = 0
    while head <= tail:
        mid = (head + tail) // 2
        count = 1
        loc = start
        for i in range(1, n):
            if arr[i] >= loc + mid:
                loc = arr[i]
                count += 1
        #if we couldn't place enough, try shorter spacing
        if count < target:
            tail = mid - 1
        #if enough routers are placed, try bigger spacing
        elif count >= target:
            best = max(best, mid)
            head = mid + 1
    return best

input = sys.stdin.readline
num_house, num_router = map(int, input().split())
addrs = []
for _ in range(num_house):
    addrs.append(int(input()))
addrs.sort()
res = binary_search(addrs, num_router)
print(res)




















        
