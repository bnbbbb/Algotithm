def solution(x, n):
    
    return [j for j in range(x, x*(n+1), x)] if x != 0 else [0]*n