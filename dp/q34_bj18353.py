#maximum increasing/decreasing array problem
n = int(input())
arr = list(map(int, input().split()))

dp = [1]

for i in range(1, n):
    best = 1
    for j in range(i):
        if arr[j] > arr[i]:
            best = max(best, dp[j] + 1)
    dp.append(best)

print(n - max(dp))
    
        


