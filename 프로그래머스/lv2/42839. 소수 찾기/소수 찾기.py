from itertools import permutations

# 소수 판별 함수
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    que = set()
    for i in range(1, len(numbers) + 1):
        perms = permutations(numbers, i)
        for j in perms:
            a = ''.join(j)
            que.add(int(a))
    for perm in set(que):
        if is_prime(perm):
            answer += 1
    return answer