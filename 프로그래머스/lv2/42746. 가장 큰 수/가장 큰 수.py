def solution(numbers):
    a = map(str, numbers)
    
    numbers = sorted(map(str, numbers), key=lambda x: x*3, reverse=True)
    answer = ''.join(numbers)
    return str(int(answer))