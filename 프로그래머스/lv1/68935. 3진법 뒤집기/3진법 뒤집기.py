def solution(n):
    answer = ''
    while n >= 1:
        answer += (str(n % 3))
        n = n//3
    a = int(answer,3)
    return a