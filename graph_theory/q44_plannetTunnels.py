import sys
from kruskal import *

input = sys.stdin.readline
numPlanet = int(input().split()[0])

planets = []
for i in range(numPlanet):
    x, y, z = list(map(int, input().split()))
    planets.append((i, x, y, z))

#sort by axis and define edges on adjacent vertices
edges = []
for i in [1,2,3]:
    sort = sorted(planets, key = lambda x: x[i])
    e = [(abs(b[i] - a[i]), a[0], b[0]) for a, b in zip(sort[:-1], sort[1:])]
    edges += e

mst = kruskal(edges, numPlanet)
total_cost = sum([e[0] for e in mst])
print(total_cost)
