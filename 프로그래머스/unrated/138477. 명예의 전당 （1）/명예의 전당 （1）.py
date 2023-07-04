def solution(k, score):
    answer = []
    b = []
    for i in score:
        if len(answer) <= k:
            answer.append(i)
            answer.sort()
        elif len(answer) > k and min(answer) > i :
            continue
        if len(answer) > k:
            del answer[0]
        b.append(min(answer))
            
            
    return b