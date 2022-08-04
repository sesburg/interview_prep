def solution(n, build_frame):
    answer = []
    def canCol(x, y):
        return y == 0 or [x-1, y, 1] in answer \
               or [x, y, 1] in answer \
               or [x, y-1, 0] in answer
    def makeCol(x, y):
        if canCol(x, y):
            answer.append([x, y, 0])
    def deleteCol(x, y):
        if len(answer) == 0:
            return False
        touching = [e for e in answer if (e[0] == x and e[1] == y + 1) or (e[0] == x-1 and e[1] == y+1)]
        answer.remove([x, y, 0])
        for t in touching:
            if t[2] == 0 and not canCol(t[0], t[1]):
                answer.append([x, y, 0])                
                return False
            if t[2] == 1 and not canBar(t[0], t[1]):
                answer.append([x, y, 0])                
                return False
        return True
        
    def canBar(x, y):
        return [x, y-1, 0] in answer or [x+1, y-1, 0] in answer \
            or ([x-1, y, 1] in answer and [x + 1, y, 1] in answer)
    def makeBar(x, y):
        if canBar(x, y):
            answer.append([x, y, 1])
    def deleteBar(x, y):
        if len(answer) == 0:
            return False
        touching = [e for e in answer if (e[0] == x-1 and e[1] == y) or (e[0] == x and e[1] == y) or (e[0] == x + 1 and e[1] == y)]
        answer.remove([x, y, 1])
        for t in touching:
            if t[2] == 0 and not canCol(t[0], t[1]):
                answer.append([x, y, 1])                
                return False
            if t[2] == 1 and not canBar(t[0], t[1]):
                answer.append([x, y, 1])                
                return False
        return True
            
    while build_frame:
        x, y, a, b = build_frame.pop(0)
        if a == 0:
            if b == 0:
                deleteCol(x, y)
            elif b == 1:
                makeCol(x, y)
        elif a == 1:
            if b == 0:
                deleteBar(x, y)
            elif b == 1:
                makeBar(x, y)
    return sorted(answer)
        