def solution(park, routes):
    
    for i,_ in enumerate(park):
        for j, _ in enumerate(park[0]):
            if 'S' == park[i][j]:
                x, y = i, j
    
    for i in routes:
        if i[0] == 'E':
            if y + int(i[1:]) < len(park[0]):
                result = [park[x][y+i] for i in range(1, int(i[1:])+1)]
                if 'X' in result:
                    continue
                else:
                    y += int(i[1:])
            else:
                
                continue
        elif i[0] == 'W':
            print(i[1:])
            if y - int(i[1:]) >= 0:
                result = [park[x][y-i] for i in range(1, int(i[1:])+1)]
                if 'X' in result:
                    continue
                else:
                    y -= int(i[1:])
            else:
                
                continue
                
        elif i[0] == 'S':
            if x + int(i[1:]) < len(park):
                print('aa')
                result = [park[x+i][y] for i in range(1, int(i[1:])+1)]
                if 'X' in result:
                    continue
                else:
                    x += int(i[1:])
            else:
                
                continue
                
        elif i[0] == 'N':
            if x - int(i[1:]) >= 0:
                result = [park[x-i][y] for i in range(1, int(i[1:])+1)]
                if 'X' in result:
                    continue
                else:
                    x -= int(i[1:])
            else:
                continue
                
    return [x, y]