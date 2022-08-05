
from collections import deque
result = []
numTest = int(input())
for _ in range(numTest):
    #setup
    numTeams = int(input())
    prevYear = list(map(int, input().split()))
    numChanged = int(input())
    changes  = []
    for _ in range(numChanged):
        changes.append(list(map(int, input().split())))

    #for each tests:
    graph = [[] for _ in range(numTeams + 1)]
    rank = []
    for t in range(len(prevYear)):
        rank.append((t + 1, prevYear[t]))
    rank = [r[1] for r in sorted(rank, key= lambda x:x[0], reverse=True)]
    top = []
    for r in range(1, len(graph)):
        #graph[a] = b means team a is ranked higher than b
        for t in top:
            graph[rank[r-1]].append(t)
        top.append(rank[r-1])
    #Apply changes
    for t1, t2 in changes:
        c1 = prevYear[t1-1]
        c2 = prevYear[t2-1]
        #switch edges
        if c1 < c2:
            graph[t1].remove(t2)
            graph[t2].append(t1)
        else:
            graph[t2].remove(t1)
            graph[t1].append(t2)
    #look for any cycles using topologic sort
    inDegree = [0] * len(graph)
    for i in range(1, len(graph)):
        for e in graph[i]:
            inDegree[e] += 1

    #print('graph', graph)
    q = deque()
    for i in range(1, len(graph)):
        if inDegree[i] == 0:
            q.append(i)
    #print('indegree', inDegree)
    answer = []
    broken = False
    while q:
        if len(q) > 1:
            broken = True
            break
        team = q.popleft()
        answer.append(team)
        for e in graph[team]:
            inDegree[e] -= 1
            if inDegree[e] == 0:
                q.append(e)
    if broken:
        result.append('?')
    elif len(answer) == numTeams:
        result.append(answer)
    else:
        result.append('IMPOSSIBLE')

for res in result:
    if res == '?' or res == 'IMPOSSIBLE':
        print(res)
    else:
        print(' '.join(list(map(str, res))))