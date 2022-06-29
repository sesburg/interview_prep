import sys
f = open(sys.argv[1], 'r')

m, n = map(int,f.readline().rstrip().split())

world = [list(map(int, f.readline().rstrip())) for _ in range(m)]
dist_log = [[999]*n for _ in range(m)]

print(f.readline().rstrip())

def bfs(x, y, curr_dist):
    if x == m - 1 and n == n - 1:
        dist_log[x][y] = curr_dist
        return None
    elif x < 0 or x > m - 1 or y < 0 or y > n - 1:
        return None 
    elif world[x][y] == 0:
        return None
    else:
        if curr_dist < dist_log[x][y]:
            dist_log[x][y] = curr_dist
            bfs(x - 1, y, curr_dist + 1)
            bfs(x + 1, y, curr_dist + 1)
            bfs(x, y - 1, curr_dist + 1)
            bfs(x, y + 1, curr_dist + 1)
        return None

bfs(0, 0, 1)
print("Result:", dist_log[m - 1][n - 1])




