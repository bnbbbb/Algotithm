def solution(strArr):
    a = [len(i) for i in strArr]
    answer = [a.count(i) for i in range(1, max(a)+1)]
    return max(answer)