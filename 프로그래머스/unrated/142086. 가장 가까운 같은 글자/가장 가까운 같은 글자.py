def solution(s):
    answer = []
    result = []
    for i, j in enumerate(s):
        x = [y for y, z in enumerate(result) if j == z]
        if j in result:
            answer.append(i-x[-1])
        else:
            answer.append(-1)
        result.append(j)
    return answer