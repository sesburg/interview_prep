#Given n x m map and player's current position,
#return the number of spaces the player moved before stopping

''''
n, m = map(int, input().split())
x, y, face = map(int, input().split())

world = [list(map(int, input().split())) for _ in range(n)]
'''

#dx and dy correspoinding to north, east, south, west
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

res = 1
visited = set()
world = None

def set_world_global(w):
    global world
    world = w

def turnleft(face):
    face = face - 1
    if face < 0:
        face = 3
    return face

def walkback(x, y, face):
    face += 2
    if face > 3:
        face = face % 2
    return x + dx[face], y + dy[face]

#Given x, y is space of the map 
#return true if player can move there
def canmove(x, y):
    return world[x][y] == 0 and (x, y) not in visited

def move(x, y, face, strikes = 0):
    global res, visited
    visited.add((x, y))
    face = turnleft(face)
    if canmove(x + dx[face], y + dy[face]):
        res += 1
        move(x + dx[face], y + dy[face], face)
    else:
        strikes += 1
        if strikes > 3:
            x, y = walkback(x, y, face)
            if world[x][y] == 0:
                move(x, y, face)
            else:
                return None
        move(x, y, face, strikes)

def return_result():
    return res

def reset_test():
    global res, visited
    res = 1
    visited = set()
#move(x, y, face)
#print(res)