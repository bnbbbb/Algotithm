def solution(m, n, board):
    answer = 0
    board = [list(row) for row in board] 
    while True:
        block_remove = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1] != '0':
                    block_remove.add((i, j))
                    block_remove.add((i, j+1))
                    block_remove.add((i+1, j))
                    block_remove.add((i+1, j+1))
        if not block_remove:
            break
        for i, j in block_remove:
            board[i][j] = '0'
            answer += 1
                    
        for i in range(m-1, 0, -1):
            for j in range(n):
                if board[i][j] == '0':
                    for k in range(i-1, -1, -1):
                        if board[k][j] != '0':
                            board[i][j] = board[k][j]
                            board[k][j] = '0'
                            break

    
    return answer