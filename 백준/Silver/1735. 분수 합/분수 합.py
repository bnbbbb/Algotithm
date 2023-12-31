import sys
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())
x = b * d // gcd(b, d)
n = a*(x//b) + c*(x//d)
r = gcd(x, n)
print(n//r, x//r)