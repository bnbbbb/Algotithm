from itertools import combinations as co

a, b = map(int, input().split())
d = list(map(int, input().split()))
li = list(co(d, 3))
result = []
for i in li:
    if b-sum(i) >= 0:
        result.append([sum(i), b-sum(i)])

x = min(result, key=lambda x: x[1])
print(x[0])