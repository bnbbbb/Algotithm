def hanoi(n, start, end, temp, answer):
    if n == 1:
        answer.append([start, end])
        return
    hanoi(n - 1, start, temp, end, answer)
    answer.append([start, end])
    hanoi(n - 1, temp, end, start, answer)

def solution(n):
    answer = []
    hanoi(n, 1, 3, 2, answer)
    return answer