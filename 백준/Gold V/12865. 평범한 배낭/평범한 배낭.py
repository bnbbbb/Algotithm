from collections import deque

n, k = map(int, input().split())
bags = [list(map(int, input().split())) for _ in range(n)]

bags.sort(key=lambda x: (x[0], x[1]))
bags = deque(bags)

dp = [0] * (k + 1)

while bags:
    w, v = bags.popleft()
    for weight in range(k, w - 1, -1):
        dp[weight] = max(dp[weight], dp[weight - w] + v)

result = dp[k]
print(result)