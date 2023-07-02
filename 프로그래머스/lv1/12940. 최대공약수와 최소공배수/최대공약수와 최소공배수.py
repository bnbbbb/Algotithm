import math
# return [math.gcd(n,m), math.lcm(n,m)]

def solution(n, m):
    count = 1
    while True:
        if (m * count) % n == 0:
            lcm = m * count
            break;
        count += 1
    gcd = max([i for i in range(1, n+1) if m % i == 0 and n % i == 0])

    return [gcd, lcm]