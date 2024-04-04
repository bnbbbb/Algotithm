def count_coin_combinations(coins, target):
    dp = [0] * (target + 1)
    dp[0] = 1  

    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] += dp[i - coin]

    return dp[target]

t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    print(count_coin_combinations(coins, m))