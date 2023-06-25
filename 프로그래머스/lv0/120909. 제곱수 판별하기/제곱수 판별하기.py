def solution(n):
    i = 1
    while i * i != n:
        i * i 
        i += 1
        if i * i > n:
            return 2
    return 1