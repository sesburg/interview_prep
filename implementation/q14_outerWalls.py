from itertools import permutations, product
def solution(n, weak, dist):
    world = [0] * n
    for w in weak:
        world[w] = 1    

    dist = sorted(dist, reverse=True)

    def covered(workers, startPoints, dirs):
        fixed = []
        for i in range(len(workers)):
            speed = workers[i]
            pos = startPoints[i]
            while speed >= 0:
                if world[pos] == 1:
                    fixed.append(pos)
                pos = (pos + dirs[i]) % n
                speed -= 1
        for i in weak:
            if i not in fixed:
                return False
        return True
    
    for i in range(len(dist)):
        workers = dist[:i + 1]
        for p in permutations(weak, i + 1):
            for q in product([1, -1], repeat=i + 1):
                if covered(workers, p, q):
                    return len(workers)
    return -1

print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
print(solution(12, [1, 5, 7], [2]))