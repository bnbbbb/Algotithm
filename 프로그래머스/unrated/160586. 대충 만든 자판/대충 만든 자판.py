def solution(keymap, targets):
    answer = []
    for i in targets:
        result = 0
        for j in i:
            a = []
            for x in keymap:
                if x.find(j) == -1:
                    continue
                a.append(x.find(j)+1)
            if len(a) > 1:
                result += min(a)
            elif len(a) == 1:
                result += a[0]
            else:
                result = -100
        
        if result >= 0:
            answer.append(result)
        else:
            answer.append(-1)
        
        
    return answer