import string
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    tmp = string.digits+string.ascii_lowercase
    answer = 0
    result = ""
    while n > 0:
        remainder = n % k
        result = tmp[remainder] + result
        n //= k
    result = result.split('0')
    for i in result:
        if i and is_prime(int(i)):
            answer += 1
    return answer
