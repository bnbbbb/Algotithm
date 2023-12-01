def triangle_type(a, b, c):
    if a == b == c == 0:
        return None
    
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return 'Equilateral'
        elif a == b or a == c or b == c:
            return 'Isosceles'
        else:
            return 'Scalene'
    else:
        return 'Invalid'

while True:
    a, b, c = map(int, input().split())
    
    result = triangle_type(a, b, c)
    
    if result:
        print(result)
    else:
        break 