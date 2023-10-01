import math

def solution(k, d):
    answer = 0
    for a in range(0, d+1, k):
        x = d * d - a * a
        cnt = math.sqrt(x) // k + 1
        answer += cnt
        
    return answer