def solution(numbers):
    numbers.sort()
    if numbers[1] < 0:
        return numbers[0] * numbers[1] if numbers[0] * numbers[1] > numbers[-1] * numbers[-2] else numbers[-1] * numbers[-2]
    else:
        return numbers[-1] * numbers[-2]