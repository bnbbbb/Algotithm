def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)
    a = []
    b = []
    for i in score:
        a.append(i)
        if len(a) == m:
            b.append(a)
            a = []
    for i in b:
        if min(i) <= k:
            answer += min(i) * m
        else:
            answer += k * m
    
    return answer