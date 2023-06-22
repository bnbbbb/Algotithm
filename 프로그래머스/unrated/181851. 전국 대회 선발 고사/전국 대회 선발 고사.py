def solution(rank, attendance):
    answer = [i if j else 'x' for i, j in zip(rank, attendance)]
    result = 0
    b = []
    for i in answer:
        if type(i) == int:
            b += [[i, answer.index(i)]]
    a = sorted(b)
    result += a[0][1] * 10000 + a[1][1] *100 + a[2][1]
    return result