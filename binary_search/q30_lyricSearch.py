from bisect import bisect_left, bisect_right
def solution(words, queries):
    def findEndpoints(arr, left, right):
        l = bisect_left(arr, left)
        r = bisect_right(arr, right)
        return l, r
        
    bin = [[] for _ in range(10001)]
    reversedBin = [[] for _ in range(10001)]
    for w in words:
        bin[len(w)].append(w)
        reversedBin[len(w)].append(w[::-1])

    answer = []
    for q in queries:
        prefix = True if q[-1]=='?' else False
        if prefix:
            w = sorted(bin[len(q)])
        else:
            w = sorted(reversedBin[len(q)])
            q = q[::-1]
        left, right = q.replace('?', 'a'), q.replace('?', 'z')
        l, r = findEndpoints(w, left, right)
        answer.append(r - l)
            
    return answer

w = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
#w2 = ["h","he","hel","hell", "hello", "hellooooo"]
#w = w + w2
q = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(w, q))