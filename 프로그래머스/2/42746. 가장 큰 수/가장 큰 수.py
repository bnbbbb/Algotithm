def solution(numbers):
    # a = map(str, numbers)
    # print(list(a))
    numbers = sorted(map(str, numbers), key=lambda x: x*4, reverse=True)
    answer = ''.join(numbers)
    return str(int(answer))