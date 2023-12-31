import sys
def primenum(n):
    while True:
        is_prime = True
        for i in range(2, int(n**(1/2))+1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime == True:
            return n
        n += 1
times = int(sys.stdin.readline())
for _ in range(times):
    n = int(sys.stdin.readline())
    if n == 1 or n == 0:
        print(2)
    else:
        result = primenum(n)
        print(result)