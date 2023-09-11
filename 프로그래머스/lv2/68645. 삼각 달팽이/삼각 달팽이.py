def solution(n):
    answer = []
    result = []
    for i in range(1, n+1):
        result.append([0]*i)
    directions = [(1, 0), (0, 1), (-1, -1)]
    direction = 0
    
    x = 0
    y = 0
    result[0][0] = 1
    for num in range(1, n*(n+1)//2+1):
        result[y][x] = num
        dy, dx = directions[direction]
        ny, nx = y+dy, x+dx
        
        if ny < 0 or ny >= n or nx < 0 or nx>=len(result[ny]) or result[ny][nx] != 0:
            direction = (direction+1) % 3
            dy, dx = directions[direction]
            ny, nx = y+dy, x+ dx
        
        y, x = ny, nx
    
    for row in result:
        answer.extend(row)
    return answer
