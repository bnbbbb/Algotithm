import sys


def primenum(n, m):
    is_prime = [True] * (m+1)
    is_prime[0], is_prime[1] = False, False
    
    for i in range(2, int(m**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, m + 1, i):
                is_prime[j] = False
    for i in range(n, m + 1):
        if is_prime[i]:
            print(i)

n, m = map(int, sys.stdin.readline().split())
primenum(n, m)