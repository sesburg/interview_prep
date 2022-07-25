import sys

input = sys.stdin.readline

num_city = int(input())
num_bus = int(input())
INF = 1e9
dist = [[INF] * (num_city + 1) for _ in range(num_city + 1)]

#initialize
for i in range(1, num_city + 1):
    dist[i][i] = 0
for i in range(num_bus):
    a, b, cost = map(int, input().split())
    dist[a][b] = min(cost, dist[a][b])

for i in range(1, num_city + 1):
    for j in range(1, num_city + 1):
        for k in range(1, num_city + 1):
            dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])

for i in range(1, num_city + 1):
    for j in range(1, num_city + 1):
        dist[i][j] = 0 if dist[i][j] == INF else dist[i][j]


for i in range(1, num_city + 1):
    res = [str(e) for e in dist[i][1:]]
    print(' '.join(res))




