#It would be faster if apples was in a set, 
#moves in a dictionary. 
n = int(input())
numApples = int(input())
apples = []
for _ in range(numApples):
    a, b = map(int, input().split())
    apples.append((a - 1, b - 1))
numMoves = int(input())
moves = {}
for _ in range(numMoves):
    t, dir = input().split()
    moves.update({t: dir})


def gameOver(head, body):
    x, y = head
    return (x, y) in body[1:] or not inBounds(x, y)

def inBounds(x, y):
    return 0 <= x < n and 0 <= y < n

time = 0
#east, south, west, north
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
facing = 0
snake = [(0, 0)]

while not gameOver(snake[0], snake):
    time += 1
    hx, hy = snake[0]
    newx, newy = hx + dx[facing], hy + dy[facing]
    if gameOver((newx, newy), snake):
        break
    if (newx, newy) in apples:
        apples.remove((newx, newy))
        snake.insert(0, (newx, newy))
    else:
        snake.insert(0, (newx, newy))
        snake.pop()
    if str(time) in moves.keys():
        m = moves[str(time)] 
        if m == 'L':
            facing = (facing - 1) % 4
        if m == 'D':
            facing = (facing + 1) % 4
print(time)




