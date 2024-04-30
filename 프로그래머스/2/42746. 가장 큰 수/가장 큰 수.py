def solution(numbers):
    if max(numbers) == 0:
        return '0'
    numbers = sorted(map(str, numbers), key=lambda x: x*3, reverse=True)
    answer = ''.join(numbers)
    return answer