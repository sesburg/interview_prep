def cut_lines(lines, cutlength):
    num_cuts = 0
    for l in lines:
        num_cuts += l // cutlength
    return num_cuts

#find the best cut using binary search
def best_cut(lines, required_cuts):
    lines = sorted(lines)
    #can't cut longer than the longest line
    head, tail = 1, lines[-1]
    best = -1
    while head <= tail:
        mid = (head + tail) // 2
        num_cuts = cut_lines(lines, mid)
        if num_cuts < required_cuts:
            tail = mid - 1
        else:
            best = max(best, mid)
            head = mid + 1
    return best

k, n = list(map(int, input().split()))
lines = []
for _ in range(k):
    lines.append(int(input()))

result = best_cut(lines, n)
print(result)