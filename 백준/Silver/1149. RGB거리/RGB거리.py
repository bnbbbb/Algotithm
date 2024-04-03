N = int(input())

cost = []
for _ in range(N):
    cost.append(list(map(int, input().split())))

for i in range(1, N):
    dp = [0] * 3
    
    dp[0] = min(cost[i-1][1], cost[i-1][2]) + cost[i][0]
    dp[1] = min(cost[i-1][0], cost[i-1][2]) + cost[i][1]
    dp[2] = min(cost[i-1][0], cost[i-1][1]) + cost[i][2]
    cost[i] = dp

print(min(cost[N-1]))