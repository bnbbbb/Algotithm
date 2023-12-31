
import sys
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
a, b = map(int, sys.stdin.readline().split())
print(a * b // gcd(a, b))