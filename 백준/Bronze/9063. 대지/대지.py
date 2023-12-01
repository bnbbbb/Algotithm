n = int(input())
x = []
y = []
for _ in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
if len(x) <= 1:
    print(0)
else:
    result = (max(x)-min(x)) * (max(y)-min(y))
    print(result)