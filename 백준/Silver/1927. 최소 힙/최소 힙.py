import heapq
import sys

n = int(sys.stdin.readline())
result = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(result, x)
    else:
        mini = heapq.heappop(result) if result else 0
        print(mini)