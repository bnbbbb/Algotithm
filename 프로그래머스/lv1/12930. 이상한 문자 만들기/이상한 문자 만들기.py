def solution(s):
    result = s.split(' ')
    answer = []
    for i in result:
        a = []
        for j in range(len(i)):
            if j % 2 ==0:
                a.append(i[j].upper())
            else:
                a.append(i[j].lower())
        answer.append(''.join(a))
    answer = ' '.join(answer)
    return answer