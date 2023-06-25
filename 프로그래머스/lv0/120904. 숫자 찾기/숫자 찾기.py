def solution(num, k):
    answer = [j for j, i in enumerate(str(num), 1) if int(i) == k]
    return answer[0] if answer else -1