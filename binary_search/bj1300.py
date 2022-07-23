
n = int(input())
k = int(input())

def binary_search(n, target):
    start, end = 1, n * n
    ans = -1
    while start <= end:
        mid = (start + end) // 2
        i = idx(n, mid)
        if target <= i:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    return ans

# return number of elements smaller or equal to x
def idx(n, x):
    res = 0
    for i in range(1, n + 1):
        res += min(x // i, n)
    return res

res = binary_search(n, k)
print(res)
    