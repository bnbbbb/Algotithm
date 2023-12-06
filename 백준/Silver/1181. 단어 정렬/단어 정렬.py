
import sys
n = int(sys.stdin.readline())

result = list(set(sys.stdin.readline().rstrip() for _ in range(n)))
result.sort(key=lambda x : (len(x), x))

for a in result:
    sys.stdout.write(f'{a}\n')