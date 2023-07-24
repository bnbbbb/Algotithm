def solution(n, left, right):
    answer = []
    
    for num in range(left, right + 1):
        row, col = divmod(num, n)
        max_val = max(row, col)
        answer.append(max_val + 1)
    
    return answer