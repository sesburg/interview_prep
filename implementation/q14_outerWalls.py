from itertools import permutations
def solution(n, weak, dist):
    world = [0] * n
    for w in weak:
        world[w] = 1    

    dist = sorted(dist, reverse=True)
    doubleWeak = weak + [w + n for w in weak]

    best = len(dist) + 1
    for start in range(len(doubleWeak)):
        for p in permutations(dist, len(dist)):
            fixed = []
            working = 0                  
            idx = start
            for w in p:
                working += 1
                pos = doubleWeak[idx] 
                cover = list(range(pos, pos + w + 1))
                while idx < len(doubleWeak) and doubleWeak[idx] <= pos + w:
                    if doubleWeak[idx] in cover:
                        fixed.append(doubleWeak[idx])
                        idx += 1
                if idx >= len(doubleWeak):
                    break
                if len(fixed) == len(weak):
                    best = min(best, working)
                    break
    if best == len(dist) + 1:
        return -1
    return best

print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
print(solution(12, [1, 5, 7], [2]))