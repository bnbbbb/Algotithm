def solution(name, yearning, photo):
    answer = []
    a = dict(zip(name, yearning))
    for i in photo:
        total = 0
        for j in i:
            for key, value in a.items():
                if j == key:
                    total += value
        answer.append(total)
    return answer