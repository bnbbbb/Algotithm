
def solution(dirs):
    result = set()
    answer = 0
    n = 5
    m = -5
    dx = {'R': 1, 'L': -1}
    dy = {'U': 1, 'D': -1}
    nx, ny = 0, 0
    for i in dirs:
        prev_x, prev_y = nx, ny
        
        if i in dx:
            if m <= nx + dx[i] <= n:
                prev_x = nx
                nx += dx[i]
            else:
                continue
        elif i in dy:
            if m <= ny + dy[i] <= n:
                prev_y = ny
                ny += dy[i]
            else:
                continue
        path = tuple(sorted([(prev_x, prev_y), (nx, ny)]))
        
        if path not in result:
            result.add(path)
            answer += 1
    return answer