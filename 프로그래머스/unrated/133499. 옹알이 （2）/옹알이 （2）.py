def solution(babbling):
    answer = 0
    tal = {'aya':1, 'ye':2, 'woo':3, 'ma':4}
    for i, _ in enumerate(babbling):
        for x, y in tal.items():
            if x in babbling[i]:
                babbling[i] = babbling[i].replace(x, str(y))
    for i, j in enumerate(babbling):
        if j.isdigit() and all( babbling[i][x-1] != babbling[i][x] for x in range(1, len(j))):
            answer += 1
    return answer