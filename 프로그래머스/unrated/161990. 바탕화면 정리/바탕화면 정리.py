def solution(wallpaper):
    x = []
    y = []
    answer = []
    for idx, i in enumerate(wallpaper):
        if '#' in i:
            y.append(i.find('#'))
            y.append(i.rfind('#'))
            x.append(idx)
    answer.append(min(x))
    answer.append(min(y))
    answer.append(max(x)+1)
    answer.append(max(y)+1)

    return answer