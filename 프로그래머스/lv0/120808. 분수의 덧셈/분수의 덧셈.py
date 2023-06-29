import math
def solution(n1, d1, n2, d2):
    answer = []
    n1, d1, n2, d2 = n1*d2, d1*d2, n2 * d1, d1*d2
    a = n1+n2
    gcd = math.gcd(n1+n2, d2)
    answer = [a//gcd, d2//gcd]
    return answer