def solution(board, moves):
    answer = 0
    result = []
    for i in moves:
        for j, _ in enumerate(board):
            if board[j][i-1] != 0:
                result.append(board[j][i-1])
                board[j][i-1] = 0
                break
    idx = 1
    while idx != len(result):
        if len(result) == 0:
            return answer
        if result[idx-1] == result[idx]:
            del result[idx]
            del result[idx-1]
            idx = 0
            answer += 2
        idx +=1
    return answer