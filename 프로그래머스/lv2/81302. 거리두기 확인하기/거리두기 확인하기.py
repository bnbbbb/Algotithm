def solution(places):
    def is_valid(x, y):
        return 0 <= x < 5 and 0 <= y < 5

    def is_safe(x, y, place):
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and place[ny][nx] == 'P':
                return False
        return True

    def check_distance(place):
        for y in range(5):
            for x in range(5):
                if place[y][x] == 'P':
                    if not is_safe(x, y, place):
                        return False
                    for i in range(5):
                        for j in range(5):
                            if place[i][j] == 'P' and (x != j or y != i) and abs(x - j) + abs(y - i) <= 2:
                                if x == j:
                                    if place[min(y, i) + 1][x] != 'X':
                                        return False
                                elif y == i:
                                    if place[y][min(x, j) + 1] != 'X':
                                        return False
                                else:
                                    if place[y][j] != 'X' or place[i][x] != 'X':
                                        return False
        return True

    result = []
    for place in places:
        if check_distance(place):
            result.append(1)
        else:
            result.append(0)
    
    return result
