def solution(k, score):
    answer = []
    b = []
    for i in score:
        b.append(i)
        b.sort()
        if len(b) > k:
            del b[0]
        answer.append(min(b))
            
            
    return answer