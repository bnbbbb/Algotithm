def solution(rows, columns, queries):
    answer = []
    
    matrix = [[i + j * columns + 1 for i in range(columns)] for j in range(rows)]
    
    for query in queries:
        y1, x1, y2, x2 = query
        
        start_value = matrix[y1-1][x1-1]
        
        min_value = start_value
        
        for y in range(y1-1, y2-1):
            matrix[y][x1-1] = matrix[y+1][x1-1]
            min_value = min(min_value, matrix[y][x1-1])
        
        for x in range(x1-1, x2-1):
            matrix[y2-1][x] = matrix[y2-1][x+1]
            min_value = min(min_value, matrix[y2-1][x])
        
        for y in range(y2-1, y1-1, -1):
            matrix[y][x2-1] = matrix[y-1][x2-1]
            min_value = min(min_value, matrix[y][x2-1])
        
        for x in range(x2-1, x1-1, -1):
            matrix[y1-1][x] = matrix[y1-1][x-1]
            min_value = min(min_value, matrix[y1-1][x])
        
        matrix[y1-1][x1] = start_value
        
        answer.append(min_value)
    
    return answer