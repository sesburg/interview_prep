def solution(words, queries):
    def binary_search(arr, query):
        #find right idx
        length = len(query)
        head, tail = 0, len(arr) - 1
        left, right = head, tail
        while head <= tail:
            mid = (head + tail) // 2
            if length < len(arr[mid]):
                tail = mid - 1
            elif length >= len(arr[mid]):
                right = mid
                head = mid + 1            
        #find left idx
        head, tail = 0, len(arr) - 1
        while head <= tail:
            mid = (head + tail) // 2
            if length <= len(arr[mid]):
                left = mid
                tail = mid - 1
            elif length > len(arr[mid]):
                head = mid + 1            
        return left, right
        
    words.sort(key = lambda x: len(x))
    answer = []
    for q in queries:
        l, r = binary_search(words, q)
        prefix = True if q[-1]=='?' else False
        to_match = q.strip('?')        
        count = 0
        for w in words[l:r+1]:
            w = w[0:len(to_match)] if prefix else w[len(q) - len(to_match):]
            if to_match in w:
                #print(to_match, w)
                count += 1
        answer.append(count)
            
    return answer

w = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
#w2 = ["h","he","hel","hell", "hello", "hellooooo"]
#w = w + w2
q = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(w, q))