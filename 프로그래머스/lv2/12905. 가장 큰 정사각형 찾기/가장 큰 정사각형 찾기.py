def solution(board):
    answer = 0
    
    rows = len(board)
    cols = len(board[0])
    
    dp = [[0] * cols for _ in range(rows)]
    
    for i in range(rows):
        dp[i][0] = board[i][0]
    for j in range(cols):
        dp[0][j] = board[0][j]
    
    for i in range(1, rows):
        for j in range(1, cols):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    for i in range(rows):
        for j in range(cols):
            answer = max(answer, dp[i][j])
    return answer ** 2  

