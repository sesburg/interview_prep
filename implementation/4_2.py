# Given N (0 <= N <= 23), return the number of times that 3 is displayed.

n = int(input())
res = 0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if "3" in str(h) + str(m) + str(s):
                res += 1

print(res)