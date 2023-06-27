def solution(sides):
    a = min(sides)
    b = max(sides)
    c = a + b
    x = list(range(b-a+1, b+1))
    y = list(range(b+1, c))
    answer = len(x) + len(y)
    
    return answer