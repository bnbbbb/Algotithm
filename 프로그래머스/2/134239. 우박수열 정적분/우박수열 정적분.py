def solution(k, ranges):
    answer = []
    idx = 1
    answer.append((0, k))
    result = []
    while k != 1:
        if k > 1 and k % 2 == 1:
            k = (k * 3) + 1
            answer.append((idx, k))
        elif k > 1 and k % 2 == 0:
            k //= 2
            answer.append((idx, k))
        else:
            answer.append((idx, k))
        idx += 1
    n = len(answer) -1
    for i in ranges:
        a, b = i[0], n + i[1]
        width = 0
        if b == a:
            result.append(0)
        elif b < a :
            result.append(-1)
        else:
            for j in range(a, b):
                x1, x2 = answer[j][1], answer[j+1][1]
                width += (x1 + x2) / 2
            result.append(width)
    return result