
import sys
from collections import deque

def josephus(n, m):
    people = deque(range(1, n+1))
    result = []

    while people:
        people.rotate(-(m-1))
        result.append(people.popleft())

    return result

n, m = map(int, sys.stdin.readline().split())

result = josephus(n, m)
result = f"<{', '.join(map(str, result))}>"
print(result)