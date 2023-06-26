import math

def solution(a, b):
    an = math.gcd(a, b)
    a, b = a // an , b // an
    if b % a == 0:
        b = b // a
    elif a % b == 0:
        return 1
    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5

    if b == 1:
        return 1
    else:
        return 2