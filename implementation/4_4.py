#Given n x m map and player's current position,
#return the number of spaces the player moved before stopping

n, m = map(int, input().split())
x, y, face = map(int, input().split())

world = [list(map(int, input().split())) for _ in range(n)]

#dx and dy correspoinding to north, east, south, west
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

print(n, m)
print(x, y, face)
print(world)

