from itertools import permutations
def solution(n, weak, dist):
    doubleWeak = weak + [w + n for w in weak]

    best = len(dist) + 1
    for start in range(len(weak)):
        for p in permutations(dist, len(dist)):
            working = 1                  
            cover = doubleWeak[start] + p[working -1]
            for idx in range(start, start + len(weak)):
                if cover < doubleWeak[idx]:
                    working += 1
                    if working > len(dist):
                        break
                    cover = doubleWeak[idx] + p[working - 1]
            best = min(best, working)
    if best == len(dist) + 1:
        return -1
    return best

print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
print(solution(12, [1, 5, 7], [2]))