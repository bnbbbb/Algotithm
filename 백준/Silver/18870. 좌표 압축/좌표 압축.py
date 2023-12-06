import sys
from collections import Counter as co
n = int(sys.stdin.readline())

result  = list(map(int, sys.stdin.readline().split()))
res = {}
for i in result:
    res[i] = 0
res = {key: n for n, key in enumerate(sorted(res.keys()))}
answer = []
for i in range(len(result)):
    answer.append(res[result[i]])
print(*answer)