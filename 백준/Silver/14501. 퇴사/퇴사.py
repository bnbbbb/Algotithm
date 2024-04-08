def max_profit(n, schedules):
    dp = [0] * (n+1)
    
    for i in range(n):
        # 현재 상담을 선택하지 않는 경우
        dp[i+1] = max(dp[i+1], dp[i])
        # 현재 상담을 선택하는 경우
        end = i + schedules[i][0]
        if end <= n:  # 퇴사 전에 상담이 끝나는 경우
            dp[end] = max(dp[end], dp[i] + schedules[i][1])
    
    return dp[n]

n = int(input())
schedules = [list(map(int, input().split())) for _ in range(n)]

print(max_profit(n, schedules))