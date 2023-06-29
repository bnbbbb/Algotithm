def solution(n):
    answer = 1
    while 7 * answer // n < 1:
        answer += 1
    return answer