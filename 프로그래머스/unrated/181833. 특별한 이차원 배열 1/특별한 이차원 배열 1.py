
def solution(n):
    answer = [[0] * n for _ in range(n)]
    for i in range(len(answer)):
        print(i)
        answer[i][i] = 1
    return answer
