def solution(n, t):
    answer = 0
    return max([ n * (2**i) for i in range(t+1)])