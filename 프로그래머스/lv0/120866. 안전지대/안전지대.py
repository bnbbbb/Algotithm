def solution(board):
    answer = []
    leng = len(board)
    for i in range(leng):
        for j in range(leng):
            if board[i][j] == 1:
                # count -=1
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        x, y = dx+i, dy+j
                        if 0 <= x < len(board) and 0 <= y <len(board) and board[x][y] != 1:
                            board[x][y] = 2
                        
    answer = len([i for i in board for j in i if j == 0])
    return answer