from collections import deque

def isSpace(board, robot):
    n = len(board)
    x, y, w, v = robot
    if 0 <= x < n and 0 <= y < n and board[x][y] == 0:
        if 0 <= w < n and 0 <= v < n and board[w][v] == 0:
            return True
    return False

def moves(board, robot):
    res = []
    x, y, w, v = robot
    #horizontal
    if abs(y - v) == 1:
        horiz = [(x, y + 1, w, v + 1), (x, y - 1, w, v - 1)]
        for i in horiz:
            if isSpace(board, i):
                res.append(i)
        vert = [(x + 1, y, w + 1, v), (x-1, y, w -1, v)]
        for i in vert:
            if isSpace(board, i):
                res.extend([i, (x, y, i[0], i[1]), (i[2], i[3], w, v)])
    #vertical   
    if abs(x - w) == 1:
        vert = [(x + 1, y, w + 1, v), (x-1, y, w -1, v)]
        for i in vert:
            if isSpace(board, i):
                res.append(i)
        horiz = [(x, y + 1, w, v + 1), (x, y - 1, w, v - 1)]
        for i in horiz:
            if isSpace(board, i):
                res.extend([i, (x, y, i[0], i[1]), (i[2], i[3], w, v)])
    return [{(x, y), (w, v)} for x, y, w, v in res]

#BFS Find shortest path
def solution(board):
    n = len(board)
    q = deque([])
    visited = []
    visited.append({(0, 0), (0, 1)})
    q.append(((0, 0, 0, 1), 0))
    while q:
        s, cost = q.popleft()
        if (s[0], s[1]) == (n - 1, n - 1) or (s[2], s[3]) == (n - 1, n - 1):
            return cost
        for m in moves(board, s):
            if m not in visited:
                visited.append(m.copy())
                a, b = m.pop(), m.pop()
                q.append(((a[0], a[1], b[0], b[1]), cost + 1))
    return None            

board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
print('Correct solution is 7, test result is {}'.format(solution(board)))



            
        




