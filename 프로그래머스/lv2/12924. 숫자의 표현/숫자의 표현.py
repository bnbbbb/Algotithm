def solution(n):
    answer = 1
    idx = 1
    while idx != n:
        total = 0
        for i in range(idx, n+1):
            total += i
            if total == n:
                answer += 1
                break
            elif total > n:
                break
        idx += 1
    return answer