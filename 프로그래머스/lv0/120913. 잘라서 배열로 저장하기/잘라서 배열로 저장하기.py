def solution(my_str, n):
    return [my_str[i*n: n*(i+1)] for i, j in enumerate(my_str) if i < (len(my_str)/n)]