def solution(a, b, n):
    answer = 0
    while n != 1:
        answer += (n // a) * b
        if n >= a:
            n = n % a + (n // a) * b
        else:
            return answer
    return answer