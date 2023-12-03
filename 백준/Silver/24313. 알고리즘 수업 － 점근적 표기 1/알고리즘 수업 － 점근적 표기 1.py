a1, a0 = map(int, input().split())

c = int(input())

n0 = int(input())

re = []
for i in range(n0, 101):
    if a1 * i + a0 > c * i:
        re.append(i)
if re:
    print(0)
else:
    print(1)