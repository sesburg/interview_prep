import sys
import heapq

input = sys.stdin.readline

num_room, num_path = map(int, input().split())

path = [[] for _ in range(num_room + 1)]
for _ in range(num_path):
    a, b = map(int, input().split())
    path[a].append(b)
    path[b].append(a)

# Run dijkstra given graph, with edge weights 1
# Return: a list of mininum distance to node i in res[i]
def dijkstra(start, graph):
    INF = 1e9
    distance = [INF for _ in range(num_room + 1)]
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    #dijkstra
    while q:
        curr_dist, curr_room = heapq.heappop(q)
        if distance[curr_room] < curr_dist:
            continue
        for room in graph[curr_room]:
            d = distance[curr_room] + 1
            if d < distance[room]:
                distance[room] = d
                heapq.heappush(q, (d, room))
    return distance[1:]

print(dijkstra(1, path))


