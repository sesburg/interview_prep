n = int(input())
houses = [0]
for _ in range(n):
    houses.append(list(map(int, input().split())))

dp = [[0]*3  for _ in range(len(houses) + 1)]

for i in range(1, n+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + houses[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + houses[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + houses[i][2]

print(min(dp[n]))