def solution(numbers, k):
    count = k
    step = 0
    while count != 1:
        numbers[0+step]
        count -= 1
        step = (step + 2) % len(numbers)
    return numbers[step]