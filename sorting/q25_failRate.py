# N < 500, stages < 200,000
def solution(N, stages):
    answer = []
    stages.sort()
    j = 0
    for i in range(1, N + 1):
        curStage = 0
        while j < len(stages) and stages[j] == i:
            curStage += 1
            j += 1
        if curStage == 0:
            answer.append((i, 0))
        else:
            answer.append((i, curStage / (len(stages) - j + curStage)))
    print('return ', answer)
    answer = sorted(answer, key=lambda x : x[1], reverse=True)
    answer = [x[0] for x in answer]
    return answer

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
print('Expected: ', [3,4,2,1,5])
print(solution(4, [4,4,4,4,4]))
print('Expected: ', [4,1,2,3])

#my tests
print(solution(3,[1, 1, 1, 2, 2, 2, 2]))
print('Expected: ', [2, 1, 3])