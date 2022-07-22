import sys
from kruskal import *

input = sys.stdin.readline
n_tests = int(input())

results = []

for _ in range(n_tests):
    n_countries, n_planes = list(map(int, input().split()))
    planes = []
    for i in range(n_planes):
        a, b = list(map(int, input().split()))
        #subtract 1 because planes are 1-indexed
        planes.append((1, a - 1, b - 1))
    mst = kruskal(planes, n_countries)
    results.append(len(mst))

for i in results:
    print(i)
