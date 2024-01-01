def is_prime(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(limit ** 0.5)+1):
        if primes[i]:
            for j in range(i*i, limit+1, i):
                primes[j] = False
    return primes

def count_primenum(n, primes):
    count = sum(primes[n+1:2*n+1])
    return count

limit = 2 * 123456
primes = is_prime(limit)

while True:
    n = int(input())
    if n == 0:
        break
    
    result = count_primenum(n, primes)
    print(result)