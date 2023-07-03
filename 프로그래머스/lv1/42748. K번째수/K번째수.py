def solution(array, commands):
    answer = []
    for i in commands:
        a, b, c = i
        x = sorted(array[a-1: b])
        answer.append(x[c-1])
    return answer 