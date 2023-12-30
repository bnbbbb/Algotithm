import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(sys.stdin.readline())
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    result = (a * b) // gcd(a, b)
    print(result)