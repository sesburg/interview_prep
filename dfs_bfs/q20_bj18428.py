def crash(map, x, y, d):
    while 0 <= x < n and 0 <= y < n:
        if map[x][y] in ["O", "T"]:
            return map[x][y]
        x, y = x + d[0], y + d[1]
    return 'E'

def isSafe(map, studs):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for x, y in studs:
        for d in dirs:
            if crash(map, x, y, d) == 'T':
                return False
    return True

def idxToCoord(n, idx):
    x = idx // n    
    y = idx % n
    return x, y

def isX(map, coord):
    return map[coord[0]][coord[1]] == 'X'

def search(n, map, students):
    for i in range(n * n - 2):
        for j in range(i + 1, n * n - 1):
            for k in range(j + 1, n * n):
                a = idxToCoord(n, i)
                b = idxToCoord(n, j)
                c = idxToCoord(n, k)
                if isX(map, a) and isX(map, b) and isX(map, c):
                    for x, y in [a, b, c]:
                        map[x][y] = 'O'
                    if isSafe(map, students):
                        print("YES")
                        return None
                    for x, y in [a, b, c]:
                        map[x][y] = 'X'
    print('NO')
            
n = int(input())
world = []
for i in range(n):
    world.append(list(input().split()))

students = []
for i in range(n):
    for j in range(n):
        if world[i][j] == 'S':
            students.append((i, j))

search(n, world, students)


