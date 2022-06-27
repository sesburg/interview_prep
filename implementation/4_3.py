# Given 8x8 chess board, starting point
# Return number of moves possible
#Time limit 1s memory 128mb

pos = input()
col, row = int(ord(pos[0]) - ord("a") +1), int(pos[1])

moves = [(1,2), (1,-2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

res = 0
for m in moves:
    c = col + m[0]
    r = row + m[1]
    if c >= 1 and r >= 1 and c <= 8 and r <= 8:
        res += 1
print(res)