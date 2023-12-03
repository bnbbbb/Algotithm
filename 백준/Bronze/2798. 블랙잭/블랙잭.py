from itertools import combinations as co

a, b = map(int, input().split())
d = list(map(int, input().split()))
li = list(co(d, 3))
result = 0
for i in li:
    current_sum = sum(i)
    if current_sum <= b and current_sum > result:
        result = current_sum
print(result)