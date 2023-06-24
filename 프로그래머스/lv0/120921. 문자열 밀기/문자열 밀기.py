def solution(m, n):
    answer = 0
    le = len(m)
    for i in range(le):
        if m != n:
            m = m[le-1:]+m[:le-1] 
            answer += 1
            if answer == len(m):
                return -1
        else:
            return answer
    return answer