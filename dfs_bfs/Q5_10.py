import sys
f = open(sys.argv[1], 'r')

m, n = map(int,f.readline().rstrip().split())

graph = []
for _ in range(m):
    graph.append(list(map(int, f.readline().rstrip())))
