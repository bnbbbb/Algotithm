def solution(numbers, target):
    total_sum = sum(numbers)  

    dp = [[0] * (2 * total_sum + 1) for _ in range(len(numbers) + 1)]

    dp[0][total_sum] = 1

    for i in range(1, len(numbers) + 1):
        for j in range(numbers[i - 1], 2 * total_sum + 1 - numbers[i - 1]):
            dp[i][j] = dp[i - 1][j - numbers[i - 1]] + dp[i - 1][j + numbers[i - 1]]

    return dp[len(numbers)][target + total_sum]