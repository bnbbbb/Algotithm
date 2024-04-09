def count_increasing_numbers(n):
    MOD = 10007
    dp = [[0] * 10 for _ in range(n+1)] 
    
    # 길이가 1인 경우 초기화
    for i in range(10):
        dp[1][i] = 1

    # 길이가 2 이상인 경우
    for i in range(2, n+1):
        for j in range(10):
            dp[i][j] = sum(dp[i-1][:j+1]) % MOD
    return sum(dp[n]) % MOD

n = int(input())
print(count_increasing_numbers(n))