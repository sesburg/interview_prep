import sys
f = open(sys.argv[1], 'r')

m, n = map(int,f.readline().rstrip().split())

graph = []
for _ in range(m):
    graph.append(list(map(int, f.readline().rstrip())))

print(f.readline().rstrip())

def dfs(x, y):
    if x < 0 or y < 0 or x > m - 1 or y > n - 1:
        return False
    if graph[x][y] == 1:
        return False
    else:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
    return True

blocks = 0
for i in range(m):
    for j in range(n):
        if dfs(i, j):
            blocks += 1

print("Result:", blocks)
