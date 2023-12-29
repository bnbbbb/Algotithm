
import sys

n, m = map(int,sys.stdin.readline().split())
result = set(sys.stdin.readline().rstrip() for _ in range(n))
answer = []
count = 0
for _ in range(m):
    a = sys.stdin.readline().rstrip()
    if a in result:
        answer.append(a)

print(len(answer))
for i in sorted(answer):
    print(i)
