def solution(places):
    def is_valid(x, y):
        return 0 <= x < 5 and 0 <= y < 5

    def check_distance(place):
        for y in range(5):
            for x in range(5):
                if place[y][x] == 'P':
                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nx, ny = x + dx, y + dy
                        if is_valid(nx, ny) and place[ny][nx] == 'P':
                            return 0
                    
                    diagonals = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
                    for dx, dy in diagonals:
                        nx, ny = x + dx, y + dy
                        if is_valid(nx, ny) and place[ny][nx] == 'P':
                            if place[y][nx] != 'X' or place[ny][x] != 'X':
                                return 0
                    
                    for dx, dy in [(0, 2), (0, -2), (2, 0), (-2, 0)]:
                        nx, ny = x + dx, y + dy
                        if is_valid(nx, ny) and place[ny][nx] == 'P':
                            if place[(y + ny) // 2][(x + nx) // 2] != 'X':
                                return 0
        return 1

    result = []
    for place in places:
        result.append(check_distance(place))
    
    return result
