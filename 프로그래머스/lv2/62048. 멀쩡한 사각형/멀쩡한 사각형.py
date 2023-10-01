import math
def solution(w,h):
    max_sq = w * h
    gcd = math.gcd(w,h)
    answer = max_sq - (w + h -gcd)
    return answer