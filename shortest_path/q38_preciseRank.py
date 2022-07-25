import sys

input = sys.stdin.readline

num_student, num_comparison = map(int, input().split())
INF = 1e9
dist = [[INF] * (num_student + 1) for _ in range(num_student + 1)]

for i in range(num_student + 1):
    dist[i][i] = 0

for _ in range(num_comparison):
    a, b = map(int, input().split())
    dist[a][b] = 1

for k in range(1, num_student + 1):
    for a in range(1, num_student + 1):
        for b in range(1, num_student + 1):
            dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])

in_out = [[0]*2 for _ in range(num_student + 1)]
for i in range(1, num_student + 1):
    for j in range(1, num_student + 1):
        if dist[i][j] != INF and dist[i][j] != 0:
            in_out[i][1] += 1 #num nodes you can reach from i
            in_out[j][0] += 1 #num nodes that can reach j

res = 0
for i in range(1, num_student + 1):
    if in_out[i][0] + in_out[i][1] == num_student - 1:
        res += 1
print(res)
        
        