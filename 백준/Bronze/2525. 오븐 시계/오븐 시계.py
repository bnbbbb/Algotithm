a, b = map(int, input().split())
tm = int(input())
h, m = divmod(tm, 60)
a, b = a + h, b + m
if b >= 60:
    a += 1
    b -= 60
if a >= 24:
    a -= 24

print(a, b)