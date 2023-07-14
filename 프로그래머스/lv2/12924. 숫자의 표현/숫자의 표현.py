def solution(n):
    answer = 1
    for i in range(1, n+1):
        result = i
        for j in range(i+1, n+1):
            result += j 
            if result == n:
                answer += 1
                break
            elif result > n:
                break
        
    return answer