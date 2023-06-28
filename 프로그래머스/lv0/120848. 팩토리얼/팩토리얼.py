def solution(n):
    i = 1
    j = 1
    while i <= n:
        j += 1
        i = i * j
    j -= 1
    return j