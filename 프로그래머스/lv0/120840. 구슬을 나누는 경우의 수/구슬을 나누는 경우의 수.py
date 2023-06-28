from math import factorial as fa
def solution(balls, share):
    answer = fa(balls) // (fa((balls-share))* fa(share))
    return answer