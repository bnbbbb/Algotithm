def solution(board):
    def check_win(symbol):
        for i in range(3):
            if all(board[i][j] == symbol for j in range(3)) or \
                all(board[j][i] == symbol for j in range(3)):
                return True
        if all(board[i][i] == symbol for i in range(3)) or \
            all(board[i][2 - i] == symbol for i in range(3)):
            return True
        return False
    count_o = sum(row.count("O") for row in board)
    count_x = sum(row.count("X") for row in board)
    # "O"가 "X"보다 많거나 "X"가 "O"보다 많으면 올바르지 않음
    if count_x > count_o or count_o > count_x + 1:
        return 0
    o_wins = check_win("O")
    x_wins = check_win("X")
    if o_wins:
        if x_wins or count_x > count_o:
            return 0
        elif not x_wins and count_x < count_o:
            return 1
    elif x_wins:
        if o_wins or count_x > count_o:
            return 0
        elif not o_wins and count_x == count_o:
            return 1

    if not x_wins and not o_wins:
        if count_x + count_o == 9:
            return 1 
        elif count_x == count_o:
            return 1 
        elif count_x == count_o - 1:
            return 1 
         
    return 0 