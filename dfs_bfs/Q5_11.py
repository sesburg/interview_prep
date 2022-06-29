import sys
f = open(sys.argv[1], 'r')

m, n = map(int,f.readline().rstrip().split())

world = [list(map(int, f.readline().rstrip())) for _ in range(m)]

print(f.readline().rstrip())



