from collections import deque

def done(fish, shark):
    if len(fish) == 0:
        return True
    elif nothingFound:
        return True
    for f in fish:
        if fish[f] < shark[2]:
            return False
    return True

def neighbor(x, y, size):
    possible = [[x-1, y], [x, y-1], [x+1, y], [x, y+1]]
    result = []
    for a, b in possible:
        if 0 <= a < len(world) and 0 <= b < len(world) and world[a][b] <= size:
            result.append((a, b))
    return result

#return distance to the closest edible fish
def bfs(shark, fish):
    global world, nothingFound, numToGrow
    q = deque()
    x, y, size = shark
    visited = []
    for n in neighbor(x, y, size):
        q.append((n, 1)) #second entry for time
        visited.append(n)
    toEat = []
    while q:
        loc, time = q.popleft()
        print(loc, time)
        if toEat and (len(fish) == 1 or time > toEat[0][2]):
            break
        x, y = loc
        if 0 < world[x][y] < shark[2]:
            # We will be sorting by y and then x
            toEat.append((x, y, time))
        else:
            for n in neighbor(x, y, size):
                if n not in visited:
                    q.append((n, time + 1))
                    visited.append((x, y))
    if len(toEat) > 0:
        x, y, time = sorted(toEat)[0]
        print(toEat)
        # print('size', shark[2])
        #delete the fish
        world[x][y] = 0
        fish.pop((x, y))
        #move and grow shark
        shark[0], shark[1] = x, y
        numToGrow -= 1
        if numToGrow == 0:
            shark[2] += 1
            numToGrow = shark[2]
        #print('ate fish at ', x, y, 'travel time :', time)
        return time 
    else:
        nothingFound = True
        return 0

worldSize = int(input())
world = []
for _ in range(worldSize):
    world.append(list(map(int, input().split()))) 

fish = {}
shark = []
#global variable to check if shark have path to edible fish
nothingFound = False
numToGrow = 2
for i in range(worldSize):
    for j in range(worldSize):
        if world[i][j] == 9:
            shark = [i, j, 2]
            world[i][j] = 0 #이거 까먹었었다
        if world[i][j] > 0:
            fish[(i, j)] = world[i][j] 
simulTime = 0
while not done(fish, shark):
    simulTime += bfs(shark, fish)
print(simulTime)







