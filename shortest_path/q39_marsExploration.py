import heapq
num_test = int(input())

def adjacent(n, x, y):
    adj = {(x-1, y), (x + 1, y), \
            (x, y-1), (x, y+1)}
    to_remove = []
    for x, y in adj:
        if x < 0 or x >= n or y < 0 or y >= n:
            to_remove.append((x, y))
    for i in to_remove:
        adj.remove(i)
    return list(adj)

# Run dijkstra on map of size nxn 
# with cost of visiting (i, j) in cost[i][j]
# Return: shortest distance from (0, 0) to (n-1, n-1)
def dijkstra(n, cost):
    dist = [[inf] * n for _ in range(n)]
    dist[0][0] = cost[0][0]
    q = []
    heapq.heappush(q, (0, 0, 0))

    while q:
        d, x, y = heapq.heappop(q)
        if dist[x][y] < d:
            continue
        for a, b in  adjacent(n, x, y):
            curr_dist = dist[x][y] + cost[a][b]
            # if distance needs updating, update and insert to queue
            if curr_dist < dist[a][b]:
                dist[a][b] = curr_dist
                heapq.heappush(q, (curr_dist, a, b))
    return dist[n - 1][n - 1]

res = []
for _ in range(num_test):
    n = int(input())
    cost = [list(map(int, input().split())) for _ in range(n)]

    inf = 1e9
    res.append(dijkstra(n, cost))

for r in res:
    print(r)







