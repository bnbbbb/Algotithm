def solution(numbers):
    answer = -1
    return sum([i for i in range(0, 10) if i not in numbers])