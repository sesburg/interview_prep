from itertools import combinations

n, m = map(int, input().split())
world = []
for i in range(n):
    world.append(list(map(int, input().split())))

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

houses, stores = [], []
for i in range(n):
    for j in range(n):
        if world[i][j] == 1:
            houses.append((i, j))
        elif world[i][j] == 2:
            stores.append((i, j))
best = 1e9
combos = combinations(stores, m)
for c in combos:
    comboSum = 0
    for h in houses:
        closest = 1e9
        for store in c:
            closest = min(closest, dist(h, store))
        comboSum += closest
    best = min(best, comboSum)
print(best)





