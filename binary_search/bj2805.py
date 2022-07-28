import sys
input = sys.stdin.readline
n, m = map(int, input().split())

trees = list(map(int, input().split()))

def cutLength(trees, cutHeight):
    res = 0
    for t in trees:
        if t - cutHeight > 0:
            res += t - cutHeight
    return res

best = 0
head = 1
tail = 1e9
while head <= tail:
    mid = (head + tail) // 2
    curr = cutLength(trees, mid)
    if curr >= m:
        best = max(best, mid)
        head = mid + 1
    else:
        tail = mid -1
print(int(best))

    

