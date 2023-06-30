def solution(n):
    answer = n ** (1/2)
    if answer == int(answer):
        answer = (answer+1) ** 2
    else:
        return -1
    return answer