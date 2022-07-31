
def neighbor(node, n):
    x, y = node
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    res = []
    for i in range(4):
        if 0 <= x + dx[i] < n and 0 <= y + dy[i] < n:
            res.append((x + dx[i], y + dy[i]))
    return res

def bfs(n, world, l, r):
    moved = False
    visited = set()
    for i in range(n):
        for j in range(n):
            if (i, j) not in visited:
                toVisit = deque([])
                currGroup = []
                currGroup.append((i, j))
                toVisit.append((i, j))
                while toVisit:
                    x, y = toVisit.popleft()
                    visited.add((x, y))
                    for a, b in neighbor((x, y), n):
                        if (a, b) not in visited and (a, b) not in toVisit \
                            and l <= abs(world[x][y] - world[a][b]) <= r:
                            currGroup.append((a, b))
                            toVisit.append((a, b))
                #print(currGroup)
                sum = 0
                if len(currGroup) > 1:
                    moved = True
                    for w, v in currGroup:
                        sum += world[w][v]
                    for w, v in currGroup:
                        world[w][v] = sum // len(currGroup)
    return moved

from collections import deque

n, l, r = map(int, input().split())
world = []
for _ in range(n):
    world.append(list(map(int, input().split())))

epoch = 0
while True:
    moved = bfs(n, world, l, r)
    if not moved:
        break
    epoch += 1
print(epoch)



                


