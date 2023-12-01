a = int(input())
b = int(input())
c = int(input())

if a==b==c==60:
    print('Equilateral')
elif (a == b or a == c or b == c) and a + b + c ==180:
    print('Isosceles')
elif a + b + c == 180 and a != b != c:
    print('Scalene')
else:
    print('Error')