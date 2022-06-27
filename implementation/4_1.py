
n = map(int, input().split())
moves = list(input().split())

start = (1,1)
R = (0, 1)
L = (0, -1)
U = (-1, 0)
D = (1, 0)

mapdict = {"R":R, "L": L, "U":U, "D":D}

def coordinateAdd(a, b):
    res_a = a[0] + b[0]
    res_b = a[1] + b[1]
    if res_a < 1 or res_a > n or res_b < 1 or res_b >n:
        return a
    return (res_a, res_b)

res = start
for m in moves:
    res = coordinateAdd(res, mapdict[m])

print(res)
