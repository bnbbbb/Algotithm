def solution(babbling):
    answer = 0
    p = ["aya", "ye", "woo", "ma"]
    
    a = babbling
    for i in range(len(a)):
        for b in p:
            if b in a[i]:
                a[i] = a[i].replace(b,' ')
        if a[i].replace(' ', '') == '':
            answer += 1
    return answer