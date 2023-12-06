import sys

n = int(sys.stdin.readline())
result = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    result.append((a, b))

result.sort(key=lambda x: (x[1], x[0]))

for a, b in result:
    sys.stdout.write(f"{a} {b}\n")