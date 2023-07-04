def solution(name, yearning, photo):
    answer = []
    a = dict(zip(name, yearning))
    for i in photo:
        total = 0
        for j in i:
            if j in a:
                total += a[j]
        answer.append(total)
    return answer