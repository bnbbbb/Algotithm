from collections import deque
import sys

arr = deque()

for line in sys.stdin.readlines()[1:]:
    n = int(line)
    if n == 0:
        arr.pop()
    else:
        arr.append(n)

print(sum(arr))